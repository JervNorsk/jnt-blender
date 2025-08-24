import logging
import inspect

from abc import ABC, abstractmethod
import types

import bpy

# -----------------------------------------------------------------------------
class JntBlenderFeature(ABC):

    def __init__(self):
        # print("Initializing " + self.__str__())
        self.logger = logging.getLogger(self.__str__())
        self.logger.setLevel(logging.INFO)
        self.logger.addHandler(logging.StreamHandler())

    @abstractmethod
    def register(self):
        pass

    @abstractmethod
    def unregister(self):
        pass

    def load_jnt_features(self, modules: object) -> tuple[type[object], object]:
        results = []

        if len(modules) > 0:
            for module in modules:
                self.logger.debug("> Looking for features in %s", module.__name__)
                for name, clazz in inspect.getmembers(module, inspect.isclass):
                    # self.logger.info("Object: %s", clazz)
                    # self.logger.info("> Is Abstract: %s", inspect.isabstract(clazz))
                    # self.logger.info("> Is Class: %s", inspect.isclass(clazz))
                    # self.logger.info("> Is JntBlenderFeature: %s", issubclass(clazz, JntBlenderFeature))
                    if not inspect.isabstract(clazz) and inspect.isclass(clazz) and issubclass(clazz, JntBlenderFeature) and clazz not in ( JntBlenderFeature, JntBlenderClass, JntBlenderModule, JntBlenderAddon ):
                        if issubclass(clazz, JntBlenderModule):
                            # self.logger.debug("> Detect %s (%s)", clazz.__qualname__, 'module')
                            pass
                        else:
                            self.logger.debug("> Detect %s (%s)", clazz.__qualname__, 'feature')
                        results.append(
                            (clazz, clazz())
                        )
        else:
            self.logger.error("> Can not loading features. Module list is empty")

        return results

class JntBlenderClass(JntBlenderFeature):

    def register(self):
        self.register_class()
        self.register_menu()

    def unregister(self):
        self.unregister_menu()
        self.unregister_class()

    @abstractmethod
    def get_classes(self) -> list[type[object]]:
        pass

    def register_class(self):
        for clazz in self.get_classes():
            self.logger.info("> Registering %s (%s) (%s)", clazz.__qualname__, "bpy", "class")
            bpy.utils.register_class(clazz)

    def unregister_class(self):
        for clazz in self.get_classes().__reversed__():
            self.logger.info("> Unregistering %s (%s) (%s)", clazz.__qualname__, "bpy", "class")
            bpy.utils.unregister_class(clazz)

    def get_menus(self) -> list[tuple[type[object], str, object]]:
        return []

    def register_menu(self):
        for clazz, parent, closure in self.get_menus():
            self.logger.info("> Registering %s (%s) (%s)", clazz.__qualname__, "bpy", "menu")
            getattr(bpy.types, parent).append(closure)

    def unregister_menu(self):
        for clazz, parent, closure in self.get_menus().__reversed__():
            self.logger.info("> Unregistering %s (%s) (%s)", clazz.__qualname__, "bpy", "menu")
            getattr(bpy.types, parent).remove(closure)

class JntBlenderModule(JntBlenderFeature):

    def __init__(self):
        super().__init__()
        # self.logger.info("-------------------------------")
        # self.logger.info("Initialize %s", '.'.join(self.__module__.split(".")[1:]))
        self.features = self.load_jnt_features(self.get_modules())

    @abstractmethod
    def get_modules(self) -> list[types.ModuleType]:
        pass

    def register(self):
        for clazz, it in self.features:
            self.logger.info("> Registering %s (%s)", clazz.__qualname__, "jnt")
            it.register()

    def unregister(self):
        for clazz, it in self.features.__reversed__():
            self.logger.info("> Unregistering %s (%s)", clazz.__qualname__, "jnt")
            it.unregister()

class JntBlenderAddon(JntBlenderFeature):

    def __init__(self, modules: object):
        super().__init__()
        self.logger.info("-------------------------------")
        self.logger.info("Initialize %s", '.'.join(self.__module__.split(".")[1:3]))
        self.logger.info("-------------------------------")
        self.features = self.load_jnt_features(modules)

    def register(self):
        self.logger.info("-------------------------------")
        self.logger.info("Registering %s", '.'.join(self.__module__.split(".")[1:3]))
        self.logger.info("-------------------------------")
        for clazz, it in self.features:
            it.register()
        self.logger.info("-------------------------------")

    def unregister(self):
        self.logger.info("-------------------------------")
        self.logger.info("Unregistering %s", '.'.join(self.__module__.split(".")[1:3]))
        self.logger.info("-------------------------------")
        for clazz, it in self.features.__reversed__():
            it.unregister()
        self.logger.info("-------------------------------")

    def reload(self):
        pass
        # reload_repository()
