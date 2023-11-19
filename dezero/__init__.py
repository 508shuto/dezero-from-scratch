is_simple_core = False

if is_simple_core:
    from dezero.core_simple import setup_variable
else:
    from dezero.core import setup_variable
setup_variable()
