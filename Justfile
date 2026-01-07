default:
    @just --list

# build app {apk, linux, web}
build platform:
    @cd examples/flet_blurhash_example && \
    uv run flet build {{ platform }}

# run result build app {apk, web} default is linux
run platform="":
    @cd examples/flet_blurhash_example && \
    uv run flet run {{ platform }} -d -r

# serve web after build app to web
serve:
    @cd examples/flet_blurhash_example && \
    uv run flet serve
