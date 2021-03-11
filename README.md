# libtest - test static library project for conan.io build system

# Requires
* conan.io 1.34

# build from cache build + publish artifact
conan create --profile:build=default --profile:host=armv7 . 0.0.1@aptera/sandbox
conan upload libtest/0.0.1@aptera/sandbox --all -r=aptera

# build from local folder only
rm -rf ./build
conan install --install-folder build --build=missing --profile:build=default --profile:host=armv7 .
conan build --build-folder build .
