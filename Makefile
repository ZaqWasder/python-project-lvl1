install:
		uv sync

brain-games:
		uv run brain-games

build:
		uv build

package-install:
	uv tool install dist/*.whl

package-uninstall:
	uv tool uninstall hexlet-code

package-reinstall: package-uninstall package-install

lint:
	uv run ruff check brain_games
