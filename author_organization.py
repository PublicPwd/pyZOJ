class AuthorOrganization:
    ID = None
    Name = None
    Comment = None
    Code = None
    Country = None
    MembersCount = None
    Type = None
    Balance = None
    Subdomain = None
    Logo = None

    def __init__(self, id, name, comment, code, country, members_count, type,
                 balance, subdomain, logo):
        self.ID = id
        self.Name = name
        self.Comment = comment
        self.Code = code
        self.Country = country
        self.MembersCount = members_count
        self.Type = type
        self.Balance = balance
        self.Subdomain = subdomain
        self.Logo = logo
