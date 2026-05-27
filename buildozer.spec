!cat <<EOF > buildozer.spec
[app]
title = My Clicker
package.name = myclicker
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy
fullscreen = 0
android.api = 33
android.minapi = 21
EOF
