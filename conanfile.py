from conan import ConanFile
from conan.tools.cmake import CMakeDeps, CMakeToolchain

class LightMaker(ConanFile):
    settings = "os", "build_type"

    def requirements(self):
        self.requires("eigen/3.4.0")
        self.requires("jsoncpp/1.9.4")
        self.requires("fmt/10.1.1")
        self.requires("tbb/2021.5")
        self.requires("nanoflann/1.5.0")
        self.requires("libcurl/8.9.1")
        self.requires("openssl/3.3.1")
        self.requires("libpng/1.6.43")
        self.requires("zlib/1.3.1")
        self.requires("minizip/1.3.1")
        self.requires("glew/2.2.0")
        self.requires("glfw/3.4")
        self.requires("openjpeg/2.5.2")
        self.requires("libjpeg-turbo/3.0.1.1")
        self.requires("zeromq/4.3.5")
        self.requires("cppzmq/4.7.1")
        self.requires("msgpack/3.3.0")
        self.requires("tinyobjloader/2.0.0-rc10")
        self.requires("tinygltf/2.9.0")
        self.requires("assimp/5.4.2")
        self.requires("opencv/4.5.5")

    def generate(self):
        tc = CMakeToolchain(self)
        tc.user_presets_path = False
        tc.generate()
        cd = CMakeDeps(self)
        cd.generate()