# Package class with self-defined variables
class Package:

    # package variables
    def __init__(self, p_id, address, city, zip, deadline, weight, notes, status, delivery_t):
        self._id = p_id
        self._address = address
        self._deadline = deadline
        self._city = city
        self._zip = zip
        self._weight = weight
        self._notes = notes
        self._status = status
        self._delivery_time = delivery_t

    # Getter / Setter functions; Complexity O(1)

    def id(self, i=None):
        if i: self._id = i
        return self._id

    def address(self, a=None):
        if a: self._address = a
        return self._address

    def city(self, c=None):
        if c: self._city = c
        return self._city

    def deadline(self, d=None):
        if d: self._deadline = d
        return self._deadline

    def zip(self, z=None):
        if z: self._zip = z
        return self._zip

    def weight(self, w=None):
        if w: self._weight = w
        return self._weight

    def notes(self, n=None):
        if n: self._notes = n
        return self._notes

    def status(self, s=None):
        if s: self._status = s
        return self._status

    def delivery_time(self, t=None):
        if t: self._delivery_time = t
        return self._delivery_time

