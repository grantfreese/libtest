from conans import ConanFile
from conan.tools.cmake import CMake, CMakeToolchain, CMakeDeps

class BuildLibtestConan(ConanFile):
	name = "libtest"
	settings = "os", "compiler", "build_type", "arch"
	exports_sources = ["src/*", "include/*"]

	def generate(self):
		tc = CMakeToolchain(self)
		tc.variables["CMAKE_SYSTEM_NAME"] = "Generic"
		tc.variables["CMAKE_SYSTEM_PROCESSOR"] = "armv7"
		tc.variables["CMAKE_TRY_COMPILE_TARGET_TYPE"] = "STATIC_LIBRARY"

		# If the source folder is missing, we're doing a local build from the recipe folder. Local
		# recipe builds have a different include path than cache builds, since the source is not
		# copied into the build/install folder during local builds.
		if(self.source_folder is None):
			# local build
			# eg, ~/work/libtest
			tc.variables["CMAKE_INCLUDE_PATH"] = self.recipe_folder
		else:
			# cache build
			# eg, ~/.conan/data/libtest/0.0.1/aptera/sandbox/build/b1b...b9f6
			tc.variables["CMAKE_INCLUDE_PATH"] = self.install_folder

		tc.generate()
		deps = CMakeDeps(self)
		deps.generate()

	def build(self):
		cmake = CMake(self)
		cmake.configure(source_folder="src")		
		cmake.build()

	def package(self):
		self.copy("include/*.h", dst="include", keep_path=True)
		self.copy("*.a", dst="lib", keep_path=False)

	def package_info(self):
		self.cpp_info.libs = ["libtest"]
		self.cpp_info.includedirs = ["."]

