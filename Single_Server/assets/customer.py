import random
from Single_Server.config import MIN_PATIENCE, MAX_PATIENCE
from Single_Server.assets.status import Status


class Customer:
    """ A class used to represent a Customer.

       It will hold all the information regarding the interaction o f this gen_customer with the whole system.
       It will hold the times at which all the events occurred for later reporting and analysis.

       Attributes
       ----------
       _id : int
           The id of the gen_customer
       patience : float
           The random value that will represent the maximum wait this gen_customer will have
       arrive : float
           The time when this gen_customer arrived
       serve : float
           The time when this gen_customer was served
       leave : float
           The time when this gen_customer left the system
       wait : float
           The time this gen_customer had to wait in line before either leaving or being served
       total_time : float
            The time this gen_customer spend in the system from the moment it arrived until it left
        status : Status
            The status in which this gen_customer is currently at

       Methods
       -------
       report() -> str
           Returns a string holding all the information hold by the gen_customer instance
   """

    def __init__(self, id: int) -> None:
        """ Constructor for gen_customer class.

            Initializes all the undefined times that will be recorded later.

            Parameters
            ----------
            id : int
                The id of the gen_customer
        """
        self._id = id
        self.patience = random.uniform(MIN_PATIENCE, MAX_PATIENCE)
        self.arrive = -1
        self.serve = -1
        self.leave = -1
        self.wait = -1
        self.total_time = -1
        self.status = Status.WAIT

    def __str__(self) -> str:
        return "Customer %02d" % self._id

    def report(self) -> str:
        """ Create a string that will hold all the information of the object to create a report.

            Returns
            -------
            str
                A string holding all the information hold by the gen_customer
        """
        self.total_time = self.leave - self.arrive
        reportVal = "Customer %02d | %s | " % (self._id, self.status)
        # reportVal += "Patience: %6.3f | " % (self.patience)
        reportVal += "Arrived: %7.3f  Left: %7.3f ==> Total time: %6.3f | " % (self.arrive, self.leave, self.total_time)
        if self.wait > 0:
            reportVal += "Waited: %6.3f | " % (self.wait)
        else:
            reportVal += " -- NO WAIT -- | "
        if self.serve != -1:
            reportVal += "Serve time: %6.3f " % (self.leave - self.serve)
        # else:
        #    reportVal += "Diff: %6.3f " % (self.leave - self.arrive)
        return reportVal

