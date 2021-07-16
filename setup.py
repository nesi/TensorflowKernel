from setuptools import setup, find_packages
from setuptools.command.install import install
import os, shutil, json

load_module = "TensorFlow/2.4.1-gimkl-2020a-Python-3.8.2"
kernel_name = load_module

class InstallCommand(install):
    def run(self):
        kernel_path = os.path.join(os.path.expanduser("~"),".local", "share", "jupyter", "kernels", kernel_name.replace("/","_"))
        wrapper_path = kernel_path + "/wrapper.sh"

        os.makedirs(kernel_path, exist_ok=True)
        shutil.copyfile("./nesi_tf_kernel/wrapper.sh", wrapper_path)

        os.chmod(wrapper_path, 0o750)
        conf_json={
                "argv": [
                    wrapper_path,
                    kernel_name,
                    "python",
                    "-m",
                    "ipykernel",
                    "-f",
                    "{connection_file}"
                ],
                "display_name": kernel_name,
                "language": "python"
            }

        with open(kernel_path + "/kernel.json", "w") as f:
            json.dump(conf_json, f)

        install.run(self)

setup(
    name="nesi_tf_kernel",
    version="1.0.0",
    description="Adds kernel to run system tensorflow.",
    url="git-repo-here",
    package_data={"nesi_tf_kernel": ["kernel.json", "wrapper.sh", "icon.svg"]},
    cmdclass={
        'install': InstallCommand,
    }
)