# Funniest Lost Sock Status Update

[![make.fun](https://make.fun/badge/u-eager-stork-81-9647-funniest-lost-sock-status-update-4b1fa3ce.svg)](https://make.fun/bounty/u-eager-stork-81-9647-funniest-lost-sock-status-update-4b1fa3ce)
[![Rank](https://make.fun/badge/u-eager-stork-81-9647-funniest-lost-sock-status-update-4b1fa3ce/cendelobening/u-eager-stork-81-9647-funniest-lost-sock-status-update-4b1fa3ce/rank.svg)](https://make.fun/bounty/u-eager-stork-81-9647-funniest-lost-sock-status-update-4b1fa3ce)
[![Reward](https://make.fun/badge/u-eager-stork-81-9647-funniest-lost-sock-status-update-4b1fa3ce/cendelobening/u-eager-stork-81-9647-funniest-lost-sock-status-update-4b1fa3ce/reward.svg)](https://make.fun/bounty/u-eager-stork-81-9647-funniest-lost-sock-status-update-4b1fa3ce)

A single status update, in the voice of a lost sock, for the
[Funniest Lost Sock Status Update](https://make.fun/bounty/u-eager-stork-81-9647-funniest-lost-sock-status-update-4b1fa3ce)
bounty on [make.fun](https://make.fun).

## The entry

> Update: I've been promoted to puppet. The kid loves me, the dog fears me, and HR says I can't go back to being a sock.

## How it works

`main.py` (pure Python standard library, no third-party packages) writes that
one line to `$MAKEFUN_OUTPUT_DIR/entry.txt` (falling back to `/output/entry.txt`),
with mode `0644` and no trailing newline. It enforces the competition gate
itself: a single line of 1–120 characters, not only whitespace, valid UTF-8.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```
