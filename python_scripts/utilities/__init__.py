class Product:
   def __init__(self, **attributes):
      self.__dict__.update(attributes)