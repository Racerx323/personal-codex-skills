# Include predicates and wildcards

## Element selectors

Selectors are relative to an element reference unless they are the standalone
`*` scope selector. `_` and `**` alone are not valid view selectors.

| Selector | Selected elements |
| --- | --- |
| `*` in an unscoped view | Top-level elements |
| `*` in `view name of parent` | The scope parent and its direct children |
| `parent.*` | All direct children of parent |
| `parent._` | Direct children related to elements already accumulated in the view |
| `parent.**` | All descendants of parent |

Selecting elements also allows the view to render relationships among the
included elements. It does not recursively include every nested descendant.
Use a qualified descendant selector when that is intended.

```likec4
views {
  view backend-overview of cloud.backend {
    include *
    include -> cloud.backend   // Add callers of the scope
    include -> *               // Incoming relationships to the scoped base set
  }
  view system-tree {
    include cloud.**           // All descendants of cloud
  }
  view services-only {
    include cloud.** where kind is service
    exclude cloud.** where tag is #deprecated
  }
}
```

Use the actual model's fully qualified identifiers and declared kinds/tags.
For example, `cloud._` is a conditional expansion, not a synonym for `cloud.*`.
Test it against the elements already included in the view.

## Relationship predicates

| Predicate | Meaning |
| --- | --- |
| `include -> element` | Incoming relationships to the selected element |
| `include element ->` | Outgoing relationships from the selected element |
| `include -> element ->` | Incoming and outgoing relationships around one selection |
| `include A <-> B` | Relationships between two selections in either direction |

Relationship predicates can bring in neighboring endpoints required to render
those relationships. They do not change what `*` means. `<-> element` is not
a valid unary form; `<->` takes two selections.

When a view omits expected elements, check scope, explicit selections, and
relationship direction before changing model data. Validate a minimal fixture
with the project's installed CLI when selector behavior is uncertain.
