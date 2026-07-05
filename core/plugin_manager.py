import os
import importlib


class PluginManager:

    def __init__(self):

        self.plugins = {}

        self.load_plugins()


    def load_plugins(self):

        folder = "plugins"


        for file in os.listdir(folder):

            if not file.endswith(".py"):
                continue

            if file == "__init__.py":
                continue


            name = file[:-3]   # define first


            try:

                module = importlib.import_module(
                    f"plugins.{name}"
                    )


                if not hasattr(
                    module,
                    "Plugin"
                ):

                    print(
                    f"[WARNING] {name} missing Plugin class"
                    )

                    continue


                self.plugins[name] = (
                    module.Plugin()
                )


                print(
                    f"[LOADED] {name}"
                )


            except Exception as e:

                print(
                f"[ERROR] Failed loading {name}: {e}"
                )

    def execute(self, user_input):

        for plugin in self.plugins.values():

            try:

                result = plugin.run(
                    user_input
                )

                if result:

                    return result

            except Exception as e:

                print(
                    f"[PLUGIN ERROR] {e}"
                )

        return None