"""
Jupyter Notebook Batch Renderer

Usage examples:
    python render_notebook.py render config.json
    python render_notebook.py render config.json --output_dir rendered
"""

from jinja2 import Environment, FileSystemLoader
import json
import fire
from pathlib import Path
from glob import glob


class NotebookRenderer:
    def render(self, config_file, output_dir="rendered"):
        """
        Render all Jupyter notebooks in current directory using configuration

        Args:
            config_file: Path to JSON configuration file
            output_dir: Output directory path (default: "rendered")
        """
        root = Path(__file__).parent.parent.parent
        print(f"Root directory: {root}")

        # Setup paths
        config_path = root / config_file
        output_path = root / output_dir

        # Create output directory if it doesn't exist
        output_path.mkdir(exist_ok=True)

        # Validate config file exists
        if not config_path.exists():
            raise FileNotFoundError(f"Config file '{config_path}' not found")

        # Load configuration
        try:
            with open(config_path, 'r') as f:
                context = json.load(f)
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON in config file: {e}")
        except Exception as e:
            raise IOError(f"Error loading config file: {e}")

        print(f"Loaded configuration: {context.keys()}")

        # Setup Jinja2 environment
        env = Environment(
            loader=FileSystemLoader(root),
            autoescape=False
        )

        # Find all .ipynb files in current directory
        ipynb_files = glob(str(root / "*.ipynb"))
        print(f"Found {len(ipynb_files)} notebook files to process")

        # Process each file
        success_count = 0
        for file_path in ipynb_files:
            try:
                file_name = Path(file_path).name
                print(f"\nProcessing: {file_name}")

                template = env.get_template(file_name)
                rendered_content = template.render(context)

                output_file = output_path / file_name
                with open(output_file, 'w') as f:
                    f.write(rendered_content)

                print(f"Successfully rendered to: {output_file}")
                success_count += 1
            except Exception as e:
                print(f"Error processing {file_name}: {str(e)}")
                continue

        print(f"\nFinished. Successfully rendered {success_count}/{len(ipynb_files)} notebooks")


if __name__ == '__main__':
    fire.Fire(NotebookRenderer)