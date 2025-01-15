.PHONY: clean test

clean:
	find . -name "__pycache__" -exec rm -r {} +
	echo "Cache cleaned."

test:
	uv run pytest -v .
