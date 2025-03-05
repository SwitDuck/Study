'''import math
class Ivent:
    def __init__(self, parameter):
        self.parameter = parameter
    def odd(self) -> bool:
        return self.parameter % 2 != 0

class Point:
    def move(self, x: float, y: float) -> None:
        self.x = x
        self.y = y
    def reset(self) -> None:
        self.move(0, 0)
    def calculate_distance(self, other:"Point") -> float:
        return math.hypot(self.x - other.x, self.y - other.y)
pointl = Point()
point2 = Point()
pointl.reset() 
point2.move(5, 0) 
print(point2.calculate_distance(pointl))'''
'''import datetime
from typing import Optional
import weakref
class TrainingData:
    def __init__(self, name: str, uploaded: datetime, tested: datetime):
        self.name = name
        self.uploaded = uploaded
        self.tested = tested
    def load(self) -> list:
        self.name = ...
class Sample:
    def __init__(self, 
                sepal_length : float,
                sepal_width: float,
                petal_length: float, 
                petal_width: float, 
                species: Optional[str] = None) -> None:
        self.sepal_length = sepal_length
        self.sepal_width = sepal_width 
        self.petal_length = petal_length
        self.petal_width = petal_width
        self.species = species
        self.classification: Optional[str] = None
    def __repr__(self) -> str:
        if self.species is None:
            known_unknown = "UnknownSample"
        else: 
            known_unknown = "KnownSample"
        if self.classification is None:
            classification = ""
        else:
            classification = f", {self.classification}"
        return(
            f" {known_unknown}(" 
            f"sepal_length={self.sepal_length}, " 
            f"sepal_width={self.sepal_width}, " 
            f"petal_length={self.petal_length}, " 
            f"petal_width={self.petal_width}, " 
            f"species={self.species!r}" 
            f"{classification}" 
            f")"
        )
    def classify(self, classification: str) -> None: 
        self .classification = classification 
    def matches(self) -> bool: 
        return self.species == self.classification
class Hyperparameter:
    """А hyperparameter value and the overall quality of the classification. """
    def __init__(self, k: int, training: "TrainingData") -> None:
        self.k = k
        self.data: weakref.ReferenceType["TrainingData"] = weakref.ref(training)
        self.quality: float
    def test(self) -> None:
        """Run the entire test suite.""" 
        training_data: Optional["TrainingData"] = self.data()
        if not training_data:
            raise RuntimeError("broken weak reference")
        pass_count, fail_count = 0, 0
        for sample in training_data.testing:
            sample.classification = self.classify(sample)
            if sample.matches():
                pass_count += 1
            else:
                fail_count += 1
        self.quality = pass_count / (pass_count + fail_count)
s2 = Sample(sepal_length=5.1, sepal_width=3.5, petal_length=1.4, petal_width=0.2, species="Iris-setosa") 
print(s2) 
s2.classification = "wrong" 
print(s2)'''


class Contact:
    all_contacts: list["Contact"] = []
    def __init__(self, name: str, email: str) -> None:
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)
    #def __repr__(self) -> str:
        #return (
           # f"{self.__class__.__name__}("f"{self.name!r}, {self.email!r}"f")"
        #)
class Supplier(Contact):
    def order(self, order: "Order") -> None:
        print(
            "if this were real system we would send "f"'{order}' order to '{self.name}'"
        )
c_1=Contact("Dusty", "dusty@example.соm")
c_2=Contact("Steve", "Steve@example.соm")
c=Contact("Some Body", "somebody@example.net")
s=Supplier("Sup Plier", "supplier@example.net")
print(c.name, c.email, s.name, s.email)
from pprint import pprint
pprint(c.all_contacts)
s.order("i need pliers")