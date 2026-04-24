---
type: meta
status: active
track: personal
lang: en
created: 2026-04-24
updated: 2026-04-24
tags: [dataview, queries, examples]
---

# Ready-to-Run Vault Queries

Open this note in Obsidian with Dataview enabled — each query runs live and stays fresh as the vault grows.

## All people, sorted by role

```dataview
TABLE status, file.mtime as "Last updated"
FROM "50-People"
WHERE type = "person"
SORT file.name ASC
```

## Active projects by track

```dataview
TABLE track, status, file.mtime as "Updated"
FROM "10-Projects"
WHERE status = "active"
SORT track ASC
```

## Everything tagged #basira

```dataview
LIST
FROM "10-Projects" OR "20-Areas" OR "30-Resources" OR "50-People"
WHERE contains(tags, "basira") OR contains(tags, "basira-sponsor") OR contains(tags, "basira-recipient") OR contains(tags, "basira-cc")
```

## Inbox items older than 7 days (audit list)

```dataview
LIST
FROM "00-Inbox"
WHERE file.ctime < date(today) - dur(7 days)
```

## Notes with missing frontmatter (for repair)

```dataview
LIST
FROM ""
WHERE !type AND file.name != "README" AND !contains(file.folder, ".obsidian")
```

## Decisions log (chronological)

```dataview
TABLE track, status, file.mtime as "Updated"
FROM ""
WHERE type = "decision"
SORT file.ctime DESC
```

## Who to contact for Basira (routing cheatsheet)

```dataview
TABLE track, file.link as "Person"
FROM "50-People"
WHERE contains(tags, "basira") OR contains(tags, "basira-sponsor") OR contains(tags, "basira-recipient") OR contains(tags, "basira-cc") OR contains(tags, "formal-owner") OR contains(tags, "patron")
```
