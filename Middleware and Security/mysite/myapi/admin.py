from django.contrib import admin

# Register your models here.

from .models import Address
from .models import Employmentdates
from .models import Event
from .models import Eventcode
from .models import Eventdetails
from .models import Id
from .models import Officer
from .models import Responsibilitydescription
from .models import Volunteer

admin.site.register(Address)
admin.site.register(Employmentdates)
admin.site.register(Event)
admin.site.register(Eventcode)
admin.site.register(Eventdetails)
admin.site.register(Id)
admin.site.register(Officer)
admin.site.register(Responsibilitydescription)
admin.site.register(Volunteer)