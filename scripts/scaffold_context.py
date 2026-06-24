import os
import json

script_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.join(script_dir, "..", "..")
context_dir = os.path.join(project_root, "context")
os.makedirs(context_dir, exist_ok=True)

files = {
    "PROJECT.md": """# PROJECT OS

## Vision
To evolve the LibraryNFC repository into a flagship-grade production application utilizing Context Engineering, Vibe Coding, and Spatial UI architecture.

## Organization
- Principal Product Designer
- Staff Android Engineer
- Google Android Framework Engineer
- Samsung Wallet Engineering Team
- Apple Wallet UX Team
- Security Engineering Team
- Performance Engineering Team
- QA Automation Team
- Release Engineering Team
- Architecture Governance Board
- Context Engineering System
- Code Review Council

## Rules of Engagement
- Every decision must be traceable, documented, verified, reversible, and regression-safe.
- Never operate statelessly. Never forget. Never guess. Never hallucinate.
- Never claim success without verification.
""",
    
    "PRD.md": """# Product Requirements Document

## Vision
A product designed by Apple Wallet, engineered by Google Android, polished by CRED, validated by an enterprise QA team.

## Target Users
- Library members requiring digital card access.
- Users expecting flagship-tier UI/UX (e.g., Apple Wallet/Samsung Wallet).

## User Personas
- **The Power User**: Wants seamless NFC emulation, rapid access, and quick settings toggles.
- **The Casual Reader**: Wants a beautiful interface that "just works" when tapping at the library.

## Core User Journeys
1. App Launch -> Home -> View Hero Card
2. Scan Card -> NFC Read -> Save to Storage
3. Enable Emulation -> Tap to Terminal -> Success/Failure Feedback

## Workflows
- **NFC Workflows**: Foreground dispatch, ReaderMode, HCE APDU transceive.
- **Biometric Workflows**: Authentication before sensitive operations.
- **Card Management**: Add, View, Switch, Delete.

## Security Requirements
- Encrypted storage for sensitive NFC payloads.

## Performance Targets
- 60 FPS UI minimum. No jank.

## Accessibility Requirements
- Full talkback support, high contrast compliance.
""",

    "ARCHITECTURE.md": """# Architecture

## Core Architectural Patterns
- **Dependency Injection**: Hilt / Dagger
- **State Management**: Kotlin Coroutines and StateFlow
- **Domain Abstraction**: Clean Architecture separation

## Module Boundaries
- `LibraryCard` (App Module): UI, ViewModels, DI
- `nfc` (Library Module): APDU parsers, ISO7816 logic, DESFire structures

## Testing Strategy
- 80%+ business logic coverage.
- UI layer tested via Espresso / Compose testing.

## Recovery Strategy
- Graceful degradation on NFC failure.
- Auto-restart of HCE service on process death.
""",

    "UI_SYSTEM.md": """# Spatial UI Operating System

The UI must feel physical, spatial, and multi-layered.

## Spatial Layer System
- **Layer 0**: Ambient Background (Subtle animated gradients)
- **Layer 1**: Content Plane (Lists, text)
- **Layer 2**: Interactive Surfaces (Buttons, toggles)
- **Layer 3**: Cards (Hero Card, Payment Card - physical properties)
- **Layer 4**: Floating Panels (Bottom sheets)
- **Layer 5**: Modals (Dialogs with backdrop blur)
- **Layer 6**: System Dialogs (Biometric prompts)
- **Layer 7**: Critical Alerts (Toasts, Snackbars)
""",

    "MOTION_SYSTEM.md": """# Motion System

A flagship motion system ensuring physical feel and 60FPS performance.

## Motion Tokens
- `duration_short`: 150ms
- `duration_medium`: 300ms
- `duration_long`: 500ms
- `easing_spring`: Damped spring physics
- `easing_decelerate`: Fast out, slow in

## Implementations
- Hero Card Shine & Tilt
- Parallax Scrolling
- Fluid Navigation Motion
- Biometric Success/Error Motion
""",

    "DESIGN_SYSTEM.md": """# Design System

## Tokens
- **Typography**: Inter/Roboto (Modern Sans-Serif)
- **Color Tokens**: Curated HSL Palette (Dark mode optimized)
- **Elevation**: 
  - `level_1`: 2dp
  - `level_2`: 4dp
  - `level_3`: 8dp
- **Glass System**: 
  - Backdrop blur, semi-transparent white/black overlays.

## Components
Every component must consume these predefined tokens. No hardcoded styling.
""",

    "TECH_DEBT.md": """# Technical Debt

1. **Legacy Storage**: Migrate plain SharedPreferences to EncryptedSharedPreferences.
2. **Fragment Lifecycle**: Ensure proper ViewLifecycleOwner usage with Coroutines.
""",

    "DECISION_LOG.md": """# Decision Log

| Date | Decision | Rationale | Status |
|------|----------|-----------|--------|
| 2026-06-24 | Establish Context OS | Directive from OMEGA MODE to ensure traceability. | Adopted |
""",

    "RELEASE_STATUS.md": """# Release Status

## Current Status: BLOCKED

### Release Blockers
- [ ] BUG-001 VERIFIED
- [ ] BUG-002 VERIFIED
- [ ] BUG-003 VERIFIED
- [ ] BUG-004 VERIFIED
- [ ] BUG-005 VERIFIED
- [ ] BUG-006 VERIFIED
- [ ] BUG-007 VERIFIED
- [ ] All Buttons Verified
- [ ] All Navigation Verified
- [ ] All Animations Verified
- [ ] All NFC Verified
- [ ] All Biometrics Verified
"""
}

json_files = {
    "FEATURE_GRAPH.json": {
        "nodes": ["Home", "Cards", "Settings", "Scan", "Clone", "Emulation", "Biometrics", "Notifications", "Overlays", "Payment"],
        "edges": []
    },
    "STATE_GRAPH.json": {
        "nodes": ["Uninitialized", "Ready", "Scanning", "Emulating", "Error"],
        "edges": []
    },
    "NAVIGATION_GRAPH.json": {
        "nodes": ["HomeFragment", "CardsFragment", "SettingsFragment"],
        "edges": []
    },
    "DEPENDENCY_GRAPH.json": {
        "nodes": ["LibraryCard", "nfc"],
        "edges": [{"source": "LibraryCard", "target": "nfc", "relation": "depends_on"}]
    },
    "BUG_GRAPH.json": {
        "bugs": [
            {"id": "BUG-001", "title": "Missing Overlay Listeners", "status": "OPEN", "severity": "HIGH"},
            {"id": "BUG-002", "title": "Overlay Logic Never Triggered", "status": "OPEN", "severity": "HIGH"},
            {"id": "BUG-003", "title": "Hidden NFC Status Card", "status": "OPEN", "severity": "MEDIUM"},
            {"id": "BUG-004", "title": "Missing Shine Animation", "status": "OPEN", "severity": "LOW"},
            {"id": "BUG-005", "title": "Duplicate Card Feedback", "status": "OPEN", "severity": "MEDIUM"},
            {"id": "BUG-006", "title": "Dead SharedFlow", "status": "OPEN", "severity": "HIGH"},
            {"id": "BUG-007", "title": "Missing UID Reveal", "status": "OPEN", "severity": "LOW"}
        ]
    },
    "ERROR_GRAPH.json": {
        "errors": []
    },
    "VERIFICATION_GRAPH.json": {
        "verifications": []
    }
}

for filename, content in files.items():
    file_path = os.path.join(context_dir, filename)
    if not os.path.exists(file_path):
        with open(file_path, "w") as f:
            f.write(content)

for filename, content in json_files.items():
    file_path = os.path.join(context_dir, filename)
    if not os.path.exists(file_path):
        with open(file_path, "w") as f:
            json.dump(content, f, indent=4)

print("Context files created successfully.")
