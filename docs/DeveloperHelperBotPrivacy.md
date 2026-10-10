---
search:
  exclude: true
hide:
  - navigation
---

# Privacy Policy: Developer Helper Bot

*Effective: October 9, 2026*

This policy covers the **developer helper bot** that Pokémon Automation maintainers run in the
[Pokémon Automation Discord server](https://discord.gg/cQ4gWxN). It is not about the Discord bot
inside the SerialPrograms app, which you run yourself and which only talks to your own server.

## What the bot is for

The bot helps the project's maintainers:

- **Find past discussions.** Maintainers @mention the bot in developer channels to ask about earlier
  bug reports and design decisions.
- **Trace test images.** Our automated tests use game screenshots that people posted when reporting
  problems. Capture cards change colors in different ways, so we need to know which capture setup
  each screenshot came from.

## What data it collects

Only from these channels of the Pokémon Automation server: #program-development, #internal-dev-chat,
#infra-development, #dev-test-data, #automation-chat and the #automation-help forum (including their
threads).

- **Message data:** message text, the author's Discord user ID and display name, the time it was sent
  (and edited), the message it replied to, the names and types of attached files, embeds, and a link
  to the message.
- **Image attachments:** only for specific messages we look up to trace where a test image came
  from. The bot downloads that message's image attachments.

The bot does not collect direct messages, member lists, presence or online status, voice data, or
anything from other servers.

## How the data is used

- To search developer discussions and answer maintainers' questions about them.
- To match test screenshots to the posts they came from, and to the capture setup the poster
  described.

To answer questions, a maintainer's question and the relevant archived messages are processed by an
AI assistant (Anthropic's Claude). We do not use the data to train AI models, and we do not use it for
advertising, profiling, or anything unrelated to developing Pokémon Automation.

## Storage and sharing

- The data is stored on a project maintainer's personal computer. It is not published, and not
  shared with, sold to or rented to anyone, apart from the AI processing described above.
- The bot only posts in Discord to reply when a maintainer @mentions it. It does not post archived
  messages or images elsewhere.
- Which capture setup a test image came from may be recorded in our public test data repository on
  GitHub. That record names the capture setup (for example "Windows with an Elgato card"), not the
  person who posted the image.

## How long data is kept

We keep the archive for as long as it is useful for developing the project, and delete it when it is
no longer needed. Downloaded images that don't match a test image are deleted once the matching is done.

## Your choices

- **Removal:** ask us to delete your messages and images from the archive, and we will.
- **Edits and deletions on Discord:** if you delete or edit a message on Discord, the archived copy
  is not updated automatically. Ask us and we will remove it.
- **Contact:** message **Gin** in the Pokémon Automation Discord server, or open an issue at
  <https://github.com/PokemonAutomation/ComputerControl/issues>.

## Changes

If this policy changes, we will update this page and its effective date.
