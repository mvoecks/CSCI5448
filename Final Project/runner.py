import User
import sqlite3

mike = User.User('Mike')
mike.setStatistic('Top 10')

mike.addToCollection('2017-12-28')
mike.addToCollection('2017-12-29')
mike.addToCollection('2017-12-30')
mike.addToCollection('2017-12-31')

mike.addToCollection('2018-07-17')
mike.addToCollection('2018-07-18')

mike.addToCollection('2018-07-21')
mike.addToCollection('2018-07-20')
mike.addToCollection('2018-07-22')

mike.addToCollection('2018-07-24')
mike.addToCollection('2018-07-25')

mike.addToCollection('2018-07-27')
mike.addToCollection('2018-07-28')

mike.addToCollection('2018-08-31')
mike.addToCollection('2018-09-01')
mike.addToCollection('2018-09-02')

mike.addToCollection('2018-10-31')
mike.addToCollection('2018-11-01')
mike.addToCollection('2018-11-02')
mike.addToCollection('2018-11-03')

mike.addToCollection('2019-07-12')
mike.addToCollection('2019-07-13')
mike.addToCollection('2019-07-14')

mike.addToCollection('2019-08-30')
mike.addToCollection('2019-08-31')
mike.addToCollection('2019-09-01')

mike.printShows()
