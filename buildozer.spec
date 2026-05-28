!cat <<EOF > buildozer.spec
[app]
title = Clicker game
package.name = myclicker 
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.3
requirements = python3,kivy
fullscreen = 0
android.api = 33
android.minapi = 21
EOF
