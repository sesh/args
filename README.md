`args` is a zero-dependency, really back to basics, solution to command line arguments in Python.

## Usage

```
import sys
from args import parse_args

args = parse_args(sys.argv[1:])
```

Arguments can be in one of three formats:

- `--option`, like `--verbose`, `--debug`
- `--value=3` to pass a value to an option
- `cmd` or any other `value` passed positionally

The output is a Python dictionary with keys for flags and options, and a `"[]"` key for all other arguments.


## Examples

```
> pipenv run python args.py test --verbose --skip=test.py
{
  "--verbose": true,
  "--skip": "test.py",
  "[]": [
    "test"
  ]
}
```

```
> pipenv run python args.py run --port=1491:1491 --volume=~/config.cfg:/etc/sonic.cfg
{
  "--port": "1491:1491",
  "--volume": "~/config.cfg:/etc/sonic.cfg",
  "[]": [
    "run"
  ]
}
```