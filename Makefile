.PHONY: clean test

clean:
	find . -name "__pycache__" -exec rm -r {} +
	echo "Cache cleaned."

test:
	echo "Test"
