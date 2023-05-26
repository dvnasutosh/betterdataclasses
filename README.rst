betterdataclass
===============

``betterdataclass`` is a Python library that enhances the functionality
of the existing ``dataclass`` system. It provides additional features
and improvements to make working with data classes even better.

Features
--------

1. StrictDictionary
~~~~~~~~~~~~~~~~~~~

The ``StrictDictionary`` class is a powerful data class that acts like a
dictionary, allowing you to store and access key-value pairs. It
enforces strict typing of the values based on the annotations of the
class attributes, ensuring data integrity and preventing type-related
bugs.

2. StrictList
~~~~~~~~~~~~~

The ``StrictList`` class is an enhanced version of the built-in list
class. It allows you to create lists with strict typing and restrictions
on the elements. You can define the allowed types or even customize
restrictions to ensure that only valid elements are added to the list.

Authors
-------

-  `@Asutosh Rath <https://www.github.com/dvnasutosh>`__

**Installation**
----------------

You can install ``betterdataclass`` using pip:

.. code:: shell

       pip install betterdataclass

**Restrictions**
----------------

-  Accepted typing Types

   -  ``Union``
   -  ``Optional``
   -  ``Final``
   -  ``Dict``
   -  ``Tuple``
   -  ``Set``
   -  ``List``
   -  ``Literal``
   -  *anything that ``typing.get_origin()`` 1 times leads to the
      aforementioned types or the default generic types*

-  Can’t produce JSON file out of ``Enum``, but it is accepted.
-  Can’t add data members post *class defination*, i.e. in *runtime*.

**Usage Example- StrictDictionary**
-----------------------------------

Let’s see a simple example of using ``betterdataclass`` to create a
strict dictionary and list.

**Creating a ``StrictDictionary``**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

   from betterdataclass import StrictDictionary

   class Person(StrictDictionary):
       name: str
       age: int

   # Create an instance of the strict dictionary
   person = Person(name='John', age=30)

   # Access the attributes
   print(person.name)  # Output: John
   print(person.age)   # Output: 30

   # Add new attribute with type checking
   person['address'] = '123 Main Street'

   # Print the strict dictionary
   print(person)       # Output: {'name': 'John', 'age': 30, 'address': '123 Main Street'}

**Creating a ``StrictList``**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

   from betterdataclass import StrictList

   class NumberList(StrictList):
       types = (int, float)

   # Create an instance of the strict list
   numbers = NumberList([1, 2, 3.14])

   # Access the elements
   print(numbers[0])   # Output: 1
   print(numbers[1])   # Output: 2
   print(numbers[2])   # Output: 3.14

   # Add new element with type checking
   numbers.append(4)

   # Print the strict list
   print(numbers)      # Output: [1, 2, 3.14, 4]

**More ``StrictDictionary`` complex Example**
---------------------------------------------

This will speed you up what are the edge capabilities of the library is.
1. ### Example 1 \```python from betterdataclass import StrictDictionary
from typing import List, Optional

::

   class Address(StrictDictionary):
       street: str
       city: str
       postal_code: str

   class Person(StrictDictionary):
       name: str
       age: int
       addresses: List[Address]
       phone: Optional[str] = None

   # Create an instance of the strict dictionary
   person = Person(
       name='John',
       age=30,
       addresses=[
           Address(street='123 Main Street', city='New York', postal_code='10001'),
           Address(street='456 Elm Street', city='Los Angeles', postal_code='90001')
       ],
       phone='555-1234'
   )

   # Access the attributes
   print(person.name)
   print(person.age)
   print(person.addresses)
   print(person.phone)

   # Add new attribute with type checking

   # Print the strict dictionary
   print(person)
   ```
   ~~``` person['email'] = 'john@example.com' ```~~
   <br>*This won't work. I can't add new data members on the go. Hence the name StrictDictionary.*

2. .. rubric:: Example 2.
      :name: example-2.

   .. code:: python

      from betterdataclass import StrictDictionary
      from typing import List, Dict, Any

      class Address(StrictDictionary):
          street: str
          city: str
          postal_code: str

      class Contact(StrictDictionary):
          email: str
          phone: str

      class Person(StrictDictionary):
          name: str
          age: int
          addresses: List[Address]
          contacts: Dict[str, Contact]
          metadata: Dict[str, Any]

      # Create an instance of the strict dictionary
      person = Person(
          name='John',
          age=30,
          addresses=[
              Address(street='123 Main Street', city='New York', postal_code='10001'),
              Address(street='456 Elm Street', city='Los Angeles', postal_code='90001')
          ],
          contacts={
              'personal': Contact(email='john@example.com', phone='555-1234'),
              'work': Contact(email='john@work.com', phone='555-5678')
          },
          metadata={
              'employee_id': 12345,
              'position': 'Manager',
              'active': True
          }
      )

      # Access the attributes
      print(person.name)
      print(person.age)
      print(person.addresses)
      print(person.contacts)
      print(person.metadata)

      # Access nested attributes
      print(person.addresses[0].street)
      print(person.contacts['personal'].email)
      print(person.metadata['position'])

3. .. rubric:: Example 3.
      :name: example-3.

   .. code:: python

          from betterdataclass import StrictDictionary
          from typing import Dict, Union, Optional

          class Address(StrictDictionary):
              street: str
              city: str
              postal_code: str

          class Contact(StrictDictionary):
              email: str
              phone: Union[str, int]

          class Person(StrictDictionary):
              name: str
              age: int
              address: Optional[Address]
              contacts: Optional[Dict[str, Union[Contact, Dict[str, str]]]]

          # Create an empty instance of the strict dictionary
          person = Person()

          # Add data using key mapping and attribute setting
          person['name'] = 'John'
          person.name = 'John'
          person['age'] = 30
          person.age = 30

          # Add nested data using key mapping
          person['address'] = Address(street='123 Main Street', city='New York', postal_code='10001')

          # Add nested data using attribute setting
          person.address = Address(street='123 Main Street', city='New York', postal_code='10001')

          # Add multiple levels of nested data using key mapping
          person['contacts'] = {
              'personal': Contact(email='john@example.com', phone='555-1234'),
              'work': {
                  'email': 'john@work.com',
                  'phone': 12345
              }
          }

          # Add multiple levels of nested data using attribute setting
          person.contacts = {
              'personal': Contact(email='john@example.com', phone='555-1234'),
              'work': {
                  'email': 'john@work.com',
                  'phone': 12345
              }
          }

          # Print the strict dictionary
          print(person)

**Usage Example- StrictList**
-----------------------------

.. _creating-a-strictlist-1:

**Creating a ``StrictList``**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

   from betterdataclass import StrictList

   class NumberList(StrictList):
       types = (int, float)

   # Create an instance of the strict list
   numbers = NumberList([1, 2, 3.14])

   # Access the elements
   print(numbers[0])   # Output: 1
   print(numbers[1])   # Output: 2
   print(numbers[2])   # Output: 3.14

   # Add new element with type checking
   numbers.append(4)

   # Print the strict list
   print(numbers)      # Output: [1, 2, 3.14, 4]

**Validation usage ``StrictList`` example**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

   from betterdataclass import StrictList
   import re

   class EmailList(StrictList):
       def restriction(self, value):
           email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
           if not re.match(email_regex, str(value)):
               return False
           return True

   # Create an instance of the EmailList
   emails = EmailList()

   # Add email values
   emails.append('john@example.com')
   emails.append('jane@example.com')
   emails.append('invalid_email')  # Throws error

   # Print the list
   print(emails)

Roadmap
-------

-  ☐ Make Validation decorators
-  ☐ Make StrictDictionary comply with Enum
-  ☐ Make it work with other dataclasses

**The Long and the short is I want generalise all the dataclass options
we got**
