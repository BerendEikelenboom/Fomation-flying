# Agent-based

Berend:
4/10

Toegevoegd: "def assign_manager"
25% agents met grootste neighbourhood zijn manager, rest contractor.
Beetje omslachtig gedaan, omdat model.get_neighbourhood je alle agents geeft (inclusief airports), dus moest zelf de airports eruit halen om alleen rekening te houden met de flights. Kunnen hiervoor een aparte definition maken, "def neighbourhood_flights" oid.

