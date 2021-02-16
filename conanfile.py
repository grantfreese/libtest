from conans import ConanFile
from conan.tools.cmake import CMake, CMakeToolchain, CMakeDeps

class BuildTestConan(ConanFile):
	name = "libtest"
	settings = "os", "compiler", "build_type", "arch"
	exports_sources = "*"
	requires = ["cmake/3.19.4"]

	def generate(self):
		tc = CMakeToolchain(self)
		tc.generate()
		deps = CMakeDeps(self)
		deps.generate()

	def build(self):
		cmake = CMake(self)
		cmake.configure()
		cmake.build()

	def package(self):
		self.copy("include/*.h", dst="include", keep_path=False)
		self.copy("*.a", dst="lib", keep_path=False)


	def package_info(self):
		self.cpp_info.libs = ["libtest"]
		#self.cpp_info.includedirs = ["inc"]
