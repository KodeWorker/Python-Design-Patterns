# Python Design Pattern

## Classification of Patterns

1. Creational Patterns
    - They work on the basis of how object can be created
    - They isolate the details of object creation
    - Code is independent of type of object to be created
    Factory, Abstract Factory, Builder, Prototype, Singleton versus Borg
    
2. Structural Patterns
    - They design the structure of object and classes so that they can compose to achieve larger results
    - The focus is on simplifying the structure and identifying the relationship between classes and objects
    - They focus on class inheritance and composition
    MVC(model-view-controller), Facade, Proxy, Decorator, Adaptor
    
3. Behavioral Patterns
    - They are concerned with the interaction among objects and responsibility of objects
    - Objects should be also be able to interact and still be loosely coupled
    Command, Interpreter, State, Chain of responsibility, Strategy, Observer, Memento, Template, Reactive design patterns

## The Factory Pattern

    **Client ---> (Interface) ---> Factory** 

    Advatages:
    - The first advandage is loose coupling in which object creation can be independent of the class implementation
    - The client need not be be aware of the class that creates the object which, in turn, is utilized by the client.
    It is only necessary to know the interface, methods, and parameters that need to be passed to create objects of the desired type.
    This simplofies implementations for the client.
    - Adding another class to the factory to create objects of another type can be easily done without the client changing the code.
    At a minimum, the client needs to pass just another parameter.
    - The factory can also reuse the existing objects. However, when the client does direct object creation, this always creates a new object.
    
    Variants:
    - Simple Factory Pattern: This allows interfaces to create objects without exposing the object creation logic.
    - Factory Method Pattern: This allows interface to create objects, but defers the decision to the subclasses to determine the class for object creation.
    - Abstract Factory Pattern: An Abstract Factory is an interface to create related objects without specifying/exposing their classes.
    The pattern provides objects of another facory, which internally creates other objects.

## The Builder Pattern

    **Director ---> Builder ---> (Concrete Builder) ---> Product** 

    Separate the construction of a complex object from  its representation so that the same construction process can create different representations.
    Building objects by assembling specifict parts.
    
## The Prototype Pattern

    **"Builder Pattern" with .clone() in the product**

    Specify the kinds of objects to use a prototypical instance, and create new objects by copying this prototype.
    It's often used when creation(initiation) of an object is costly.
    
    Watch out for the difference of copy and deepcopy in python!

## The Singleton and Borg Design Pattern

    Singletons are typically used in the cases need to have only one instance that is available across the application to avoid conflicting requests on the same resource.

    - Ensuring that one and only one object of the class gets created
    - Providing an access point for an object that is global to the program
    - Controlling concurrent access to resources that are shared
    
    The Borg Idiom (a.k.a monostate pattern) lets a class have as many instances as one likes, but ensure that they all share the same state.
    
    Object creation vs. object initiation
    - **__new__** is the first step of instance creation; it's called before __init__, and is responsible for returing a new instance of your class
    - **__init__** dosen't return anything; it's only responsible for initializing the instance after it's been created.
    
    Comparison between Singleton and Borg
    - Singleton: 
        - Pros: allocated only once (mem. efficent), policies can be added to the method for accessing singlton pointer
        - Cons: Derivatives of Singletons are not automatically Singleton (need to overriding methods), must always be accessed through a pointer or reference
    - Borg:
        - Pros: Derivatives of Borg are also Borg, Access Borg does not have to be through pointers or references.
        - Cons: allocated/deallocated many times, no instantiation policy can exist
    
    Python modules are singletons! But it's generally not a good idea to us them for the Singleton pattern.
    - Error-prone: if you forget local and global statements, it will create confusions.
    - They pollute the module namespace
    - No OOP benefits like associated methods or reuse through inheritance
    
# Reference:

1. **LearningPython Design Patterns - Second Edition**
by Chetan Giridhar, Packt Publishing, Feb. 2016

2. **Python Design Patterns**
by Tong Qiu, Packt Publishing, 2017
