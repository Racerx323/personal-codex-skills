# Bidirectional relationships and view predicates

## Model and deployment declarations

`A <-> B` declares one semantic bidirectional relationship in a model or
between deployment nodes/instances. It is valid in LikeC4 1.59.4.
Two declarations, `A -> B` and `B -> A`, instead represent two separately
identified directed relationships with potentially different titles or kinds.

```likec4
specification {
  element service
  relationship sync
}
model {
  frontend = service
  backend = service
  frontend -[sync]<-> backend "replicates"
}
```

Use `A -> B` when A initiates a call; a routine response does not require a
second model relationship. Dynamic views can show the response as `A <- B`.
Choose a bidirectional declaration for a single mutual interaction, or two
separate directed declarations when the model needs to distinguish them.

A relationship kind uses `A -[kind]-> B`, `A -[kind]<-> B`, or the directed
shorthand `A .kind B`; do not add another arrow after `.kind`.

## Relationship predicates in views

View predicates select existing relationships; they do not declare new ones.

| Predicate | Meaning |
| --- | --- |
| `-> X` | Incoming relationships to X, including bidirectional relationships involving X |
| `X ->` | Outgoing relationships from X |
| `-> X ->` | Incoming and outgoing relationships of X |
| `A <-> B` | Relationships between the two element sets in either direction |

```likec4
views {
  view frontend-detail {
    include -> frontend ->
    include frontend <-> backend
  }
}
```

`<-> X` is not a valid unary view predicate. Use `-> X ->` for neighbors
in both directions, or `A <-> B` when selecting between two known sets.
