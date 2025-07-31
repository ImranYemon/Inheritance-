🧬 Inheritance in Python (OOP)
Inheritance is one of the core concepts in Object-Oriented Programming. It allows a class to inherit properties and behavior (attributes and methods) from another class.

🔹 What is Inheritance?
Inheritance means creating a new class (called a child or subclass) based on an existing class (called a parent or superclass).
The child class gets all the features of the parent class automatically and can also add or modify features.

✅ Why Use Inheritance?
Reusability: You don’t have to rewrite common code.

Extendability: You can easily build upon existing code.

Organized code: Keeps related logic grouped together.

🏗️ Real-Life Example
Imagine a general class Animal. All animals can eat and sleep.
Now you create a Dog class that inherits from Animal.
You don’t need to rewrite the eat/sleep methods — the Dog class gets them automatically — and you can also add a new method like bark().

🔄 Types of Inheritance in Python
Single Inheritance: One child inherits from one parent.

Multiple Inheritance: One child inherits from multiple parents.

Multilevel Inheritance: A child inherits from a parent, and then another child inherits from that child.

Hierarchical Inheritance: Multiple children inherit from the same parent.

Hybrid Inheritance: A combination of the above types.

🔐 Important Notes
The parent class is usually more general, while the child class is more specific.

You can override methods in the child class to customize behavior.
