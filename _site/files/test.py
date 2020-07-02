from Testing.makerequest import makerequest
from AccessControl.SecurityManagement import newSecurityManager
from Products.ZSQLMethods.SQL import manage_addZSQLMethod

app = makerequest(app)
portal = app.root
user = app.acl_users.getUser("cieadmin")
user = user.__of__(app.acl_users)
newSecurityManager(None, user)

sql = "select name from candidates where name like '%montserrat%';"
sql = """SELECT DISTINCT Candidates.Name
FROM         Candidates INNER JOIN
                      CandidateEntries ON Candidates.CanSid = CandidateEntries.CanSid
WHERE     (CandidateEntries.CnuId = 'CH140')"""
manage_addZSQLMethod(portal, "migrate", "Migrate the SQL", "MSSQL", None, sql)
results = portal.migrate()
portal.manage_delObjects(["migrate",])
    
for result in results:
    print result.name.decode("latin-1", "ignore")

