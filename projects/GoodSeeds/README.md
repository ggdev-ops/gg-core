# GoodSeeds App

**Repository:** [ggdev-ops/GoodSeeds](https://github.com/ggdev-ops/GoodSeeds)

## Executive Summary

GoodSeeds provides simple, beautiful, and fully offline calming experiences that respect user privacy. The app uses a clean MVVM architecture with thread-safe Manager classes protected by a Mutex and exposes immutable state snapshots to the Compose UI via StateFlow. Content is loaded from local resources only; there are no accounts, analytics, or cloud dependencies.

## Features

### Be Calm (cards)
- Dynamic batches of 2–7 cards, deterministic daily pool
- Vibe filtering, progress tracking, offline content
- Touch/hold interactions and cozy animations

### Baby Sitter (Android-first)
- Presets (Nap, Soothing, Playtime) with durations and themes
- Start/Pause/Resume/Stop with accurate 1s ticker
- Active Session screen with timer, progress, and calming visuals
- Session history (last 10) and last preset persistence
- EN/AR basics, RTL-friendly UI foundations