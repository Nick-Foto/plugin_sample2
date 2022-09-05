import plugin_spec as hookspecs
import plugin_impl as hookimpl
import pluggy


def get_plugin_manager():
    pm = pluggy.PluginManager(project_name="datastore")
    pm.add_hookspecs(hookspecs)
    pm.register(hookimpl)
    pm.load_setuptools_entrypoints("datastore")
    return pm

pm = get_plugin_manager()
pm.hook.print_output(config="test_config")
