# WasWhereWhen is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# WasWhereWhen is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with WasWhereWhen.  If not, see <http://www.gnu.org/licenses/>.
#
from django.db import models

class Person(models.Model):
    individual = models.CharField(max_length=128)

class Alias(models.Model):
    person = models.ForeignKey(Person)
    alias = models.CharField(max_length=64)
