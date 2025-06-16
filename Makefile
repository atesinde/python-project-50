build: # сборка пакета
	uv build
package-install: # установка пакета
	uv tool install dist/*.whl
package-reinstall: # переустановить пакет после изменений
	uv tool install --force dist/hexlet_code-0.1.0-py3-none-any.whl