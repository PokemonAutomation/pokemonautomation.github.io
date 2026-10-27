# Enabled Markdown Extensions

Use callouts (also called **admonitions**) to highlight setup requirements, troubleshooting advice, and examples in the PokémonAutomation wiki.

These extensions are already enabled in `mkdocs.yml`:

- `admonition`: callout boxes.
- `pymdownx.details`: callouts readers can expand or collapse.
- `pymdownx.superfences`: fenced code blocks inside callouts and other nested content.

This guide follows the [Material for MkDocs admonitions reference](https://squidfunk.github.io/mkdocs-material/reference/admonitions/). Preview the published wiki or a local MkDocs build to see the styled boxes; GitHub's Markdown preview does not render this syntax as callouts.

## Basic syntax

Start with `!!!` and a type. Leave a blank line, then indent the body by **four spaces**. Keep every paragraph, list, or code block inside that indentation; unindented text ends the callout.

```markdown
!!! note

    Check the program's wiki page for its required in-game settings.
```

!!! note

    Check the program's wiki page for its required in-game settings.

## Choose a type

Material provides the following 12 types, each with its own styling and icon. The suggested uses below are writing guidance for our wiki. Each example includes Markdown to copy and the resulting callout.

Use these canonical names: older aliases such as `summary`, `hint`, and `error` are deprecated in Material. Unknown types fall back to `note` styling.

### `note` — general reminders

```markdown
!!! note "Check the program instructions"

    Read the [program's wiki page](../Programs/index.md) before changing its options.
```

!!! note "Check the program instructions"

    Read the [program's wiki page](../Programs/index.md) before changing its options.

### `abstract` — a short overview

```markdown
!!! abstract "What to include in a bug report"

    Include the application version, program name, options, and logs from the failed run.
```

!!! abstract "What to include in a bug report"

    Include the application version, program name, options, and logs from the failed run.

### `info` — background information

```markdown
!!! info "Where to find past logs"

    `SerialPrograms.log` is in the folder where you launch the application.
```

!!! info "Where to find past logs"

    `SerialPrograms.log` is in the folder where you launch the application.

### `tip` — helpful advice

```markdown
!!! tip "Capture a useful screenshot"

    Use the application's Screenshot button when reporting a visual detection issue.
```

!!! tip "Capture a useful screenshot"

    Use the application's Screenshot button when reporting a visual detection issue.

### `success` — a successful result

```markdown
!!! success "Screenshot ready"

    After taking a screenshot, look for a file starting with `screenshot-` in the application folder.
```

!!! success "Screenshot ready"

    After taking a screenshot, look for a file starting with `screenshot-` in the application folder.

### `question` — FAQs and troubleshooting questions

```markdown
!!! question "What should I check after a program stops unexpectedly?"

    Compare your settings with the program's wiki page, then collect the relevant logs.
```

!!! question "What should I check after a program stops unexpectedly?"

    Compare your settings with the program's wiki page, then collect the relevant logs.

### `warning` — a precaution before continuing

```markdown
!!! warning "Preserve the current session's logs"

    Copy the relevant Output Window logs before closing the application. Reopening it clears that window's history.
```

!!! warning "Preserve the current session's logs"

    Copy the relevant Output Window logs before closing the application. Reopening it clears that window's history.

### `failure` — an unsuccessful result and next steps

```markdown
!!! failure "Visual detection failed"

    If a debug image was saved, include it from `ErrorDumps` along with the logs when reporting the failure.
```

!!! failure "Visual detection failed"

    If a debug image was saved, include it from `ErrorDumps` along with the logs when reporting the failure.

### `danger` — a risk of irreversible loss

```markdown
!!! danger "Check before releasing Pokémon"

    Before running a release program, verify that its target boxes contain no Pokémon you want to keep.
```

!!! danger "Check before releasing Pokémon"

    Before running a release program, verify that its target boxes contain no Pokémon you want to keep.

### `bug` — a software issue or debugging information

```markdown
!!! bug "Reporting a reproducible issue"

    Describe the steps that trigger the issue and follow the [bug reporting guide](ReportBug.md).
```

!!! bug "Reporting a reproducible issue"

    Describe the steps that trigger the issue and follow the [bug reporting guide](ReportBug.md).

### `example` — a concrete demonstration

```markdown
!!! example "A useful report title"

    A title such as “Egg hatching stops after a party check” is more useful than “It broke.”
```

!!! example "A useful report title"

    A title such as “Egg hatching stops after a party check” is more useful than “It broke.”

### `quote` — quoted text

```markdown
!!! quote "Example user report"

    “The program stopped immediately after checking my party. I attached the logs and error image.”
```

!!! quote "Example user report"

    “The program stopped immediately after checking my party. I attached the logs and error image.”

The report above is illustrative. When quoting an actual report or another guide, credit and link to its source.

## Customize the title

The default title is the type name, such as **Note**. Add a quoted title after the type, as in the gallery, to make it specific. Use `""` to omit both title and icon on a regular callout:

```markdown
!!! info ""

    See the program's wiki page for the full setup checklist.
```

!!! info ""

    See the program's wiki page for the full setup checklist.

Collapsible blocks need a visible title; the empty-title form does not apply to them.

## Collapsible blocks with `pymdownx.details`

Replace `!!!` with `???` for a block that starts closed, or `???+` for one that starts open. Both allow the reader to toggle the content. The types and four-space indentation stay the same.

Use a closed block for optional troubleshooting detail:

```markdown
??? question "Where can I get logs after a crash?"

    Open `SerialPrograms.log` in the application folder and find the timestamps around the failure.
```

??? question "Where can I get logs after a crash?"

    Open `SerialPrograms.log` in the application folder and find the timestamps around the failure.

Use an initially open block for a checklist readers may want to collapse later:

```markdown
???+ tip "Bug report checklist"

    - Application version and program name
    - Program options and in-game settings
    - Relevant logs and screenshots
```

???+ tip "Bug report checklist"

    - Application version and program name
    - Program options and in-game settings
    - Relevant logs and screenshots

Keep essential setup steps and warnings visible with `!!!`. Readers should not have to expand a box to discover a risk of losing Pokémon or progress.

## Code inside callouts with `pymdownx.superfences`

[SuperFences](https://facelessuser.github.io/pymdown-extensions/extensions/superfences/) supports fenced code inside callouts, details, and lists. Indent the opening fence, code, and closing fence with the callout body. Add a language after the opening fence, such as `cpp`, `json`, or `text`.

The outer four-backtick fence below lets this guide display an example containing triple backticks. Copy only the content inside that outer fence:

````markdown
!!! example "Wait for queued controller commands"

    In a button script, wait for queued commands to finish before continuing:

    ```cpp
    context.wait_for_all_requests();
    ```

    See [Send Button Commands](Button.md) for context.
````

!!! example "Wait for queued controller commands"

    In a button script, wait for queued commands to finish before continuing:

    ```cpp
    context.wait_for_all_requests();
    ```

    See [Send Button Commands](Button.md) for context.

The same indentation works inside `???` and `???+` blocks, which is useful for optional sample logs or configuration snippets.

## Nesting callouts

Indent an inner callout by another four spaces. Keep nesting shallow so the instructions remain easy to follow.

```markdown
!!! info "Preparing a bug report"

    Gather the logs around the failure.

    !!! tip "Include the error image"

        Check `ErrorDumps` for an image whose timestamp matches the failure.
```

!!! info "Preparing a bug report"

    Gather the logs around the failure.

    !!! tip "Include the error image"

        Check `ErrorDumps` for an image whose timestamp matches the failure.

## Before submitting a wiki edit

- Preview the page in MkDocs and check that each example renders as intended.
- If text falls outside a box, check its indentation and blank lines.
- If code is parsed as ordinary text, check that both fences are indented equally.
- Use callouts selectively: keep the main procedure in the page body and highlight the details readers need most.
