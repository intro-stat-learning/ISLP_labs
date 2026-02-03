#!/usr/bin/env python

import argparse
import subprocess
import sys
import tempfile
from pathlib import Path

def run_command(command, cwd):
    """Runs a command and prints its output."""
    print(f"Running command: {' '.join(command)} in {cwd}")
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, cwd=cwd, text=True)
    for line in iter(process.stdout.readline, ''):
        print(line, end='')
    process.wait()
    if process.returncode != 0:
        raise subprocess.CalledProcessError(process.returncode, command)

def setup_env(outdir, 
              commit, 
              python_version, 
              nbfiles,
              uv_executable,
              nbmake_timeout,
              nbmake_kernel,
              nbmake_allow_errors,
              nbmake_rerun):
    """
    Sets up a student environment for ISLP_labs.

    Parameters
    ----------
    outdir : Path
        Output directory.
    commit : str
        Commit hash or tag to checkout.
    python_version : str
        Python version to use for the virtual environment.
    nbfiles : list
        List of notebook files to run with nbmake.
    uv_executable : str
        The `uv` executable.
    nbmake_timeout : int
        Timeout for running notebooks with nbmake.
    nbmake_kernel : str
        Kernel to use for running notebooks with nbmake.
    nbmake_allow_errors : bool
        Allow errors when running notebooks with nbmake.
    nbmake_rerun : int
        Number of times to rerun notebooks with nbmake.
    """
    repo_url = 'https://github.com/intro-stat-learning/ISLP_labs.git'

    if outdir is None:
        with tempfile.TemporaryDirectory() as tmpdir:
            setup_env(Path(tmpdir), 
                      commit, 
                      python_version, 
                      nbfiles,
                      uv_executable,
                      nbmake_timeout,
                      nbmake_kernel,
                      nbmake_allow_errors,
                      nbmake_rerun)
        return
    
    if not outdir.exists():
        outdir.mkdir(parents=True)

    try:
        print(f"Initializing repository in {outdir}...")
        run_command(['git', 'init'], cwd=str(outdir))
        run_command(['git', 'remote', 'add', 'origin', repo_url], cwd=str(outdir))

        print(f"Fetching commit {commit}...")
        run_command(['git', 'fetch', 'origin', commit, '--depth=1'], cwd=str(outdir))
        
        print(f"Checking out commit {commit}...")
        run_command(['git', 'checkout', 'FETCH_HEAD'], cwd=str(outdir))

        print(f"Setting up Python {python_version} with {uv_executable}...")
        run_command([uv_executable, 'python', 'install', python_version], cwd=str(outdir))

        print("Creating virtual environment...")
        run_command([uv_executable, 'venv', '--python', python_version, '--seed'], cwd=str(outdir))

        print("Installing requirements...")
        venv_dir = Path('.venv')
        uv_bin = venv_dir / 'Scripts' if sys.platform == 'win32' else venv_dir / 'bin' 
        
        run_command([str(uv_bin / 'pip'), 'install', '-r', 'requirements.txt', 'jupyterlab'], cwd=str(outdir))
        
        if nbfiles:
            run_command([str(uv_bin / 'pip'), 'install', 'pytest', 'nbmake'], cwd=str(outdir))
            for nbfile in nbfiles:
                notebook_path = outdir / nbfile
                if not notebook_path.exists():
                    print(f"Error: Notebook '{nbfile}' not found in the repository.", file=sys.stderr)
                    continue

                print(f"Running notebook {notebook_path}...")
                pytest_command = [str(uv_bin / 'pytest'), '--nbmake', f'--nbmake-timeout={nbmake_timeout}', '-vv', str(nbfile)]
                if nbmake_kernel:
                    pytest_command.append(f'--nbmake-kernel={nbmake_kernel}')
                if nbmake_allow_errors:
                    pytest_command.append('--nbmake-allow-errors')
                if nbmake_rerun > 0:
                    pytest_command.append(f'--nbmake-rerun={nbmake_rerun}')

                run_command(pytest_command, cwd=str(outdir))

        print("Setup completed successfully.")
        print(f"Environment is in: {outdir}")
        if sys.platform == 'win32':
            print(f"Activate it with: .\\{outdir.name}\\.venv\\Scripts\\activate")
        else:
            print(f"Activate it with: source {outdir.name}/.venv/bin/activate")


    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}", file=sys.stderr)
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description='Setup a student environment for ISLP_labs.')
    parser.add_argument('--outdir', type=Path, default=None, help='The output directory to checkout the labs (default: a temporary directory)')
    parser.add_argument('--commit', default='main', help='The git commit, tag, or branch to checkout (default: main)')
    parser.add_argument('--python-version', default='3.11', help='Python version to use (default: 3.11)')
    parser.add_argument('--uv-executable', default='uv', help='The `uv` executable to use (default: "uv")')
    parser.add_argument('--nbmake-timeout', type=int, default=3600, help='Timeout for running notebooks with nbmake (default: 3600)')
    parser.add_argument('--nbmake-kernel', default=None, help='Kernel to use for running notebooks with nbmake')
    parser.add_argument('--nbmake-allow-errors', action='store_true', help='Allow errors when running notebooks with nbmake')
    parser.add_argument('--nbmake-rerun', type=int, default=0, help='Number of times to rerun notebooks with nbmake')

    parser.add_argument('nbfiles', nargs='*', help='Optional list of notebooks to run using nbmake.')

    args = parser.parse_args()
    
    setup_env(args.outdir, 
              args.commit, 
              args.python_version, 
              args.nbfiles,
              args.uv_executable,
              args.nbmake_timeout,
              args.nbmake_kernel,
              args.nbmake_allow_errors,
              args.nbmake_rerun)

if __name__ == '__main__':
    main()
