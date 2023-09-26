"""My docstring"""


class MyClass:
  """ Docstring of A"""

  def __init__(self, a_var: int) -> None:
      self._a_var = a_var

  @property
  def a_var(self) -> int:
    return self._a_var
    
