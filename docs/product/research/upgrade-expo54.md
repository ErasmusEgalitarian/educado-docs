# 📱 Upgrade and Refactor of the Mobile Application  
_Author: Martin Kedmenec_  

---

## 🎯 Introduction and Rationale
- **Technical Debt**: Outdated branches, dependencies (2–3 years old), inconsistent styles, old directory structure, no TypeScript.  
- **Google Play Requirement**: New apps must target **Android 15 (API 35)** → impossible in current state.  
- **Impact**: Outdated practices caused bugs, slowed development, and made deployments unreliable.  
- **Key Question**: **How can we fix this?**  

---

## ⚡ Initial Upgrade and Challenges
- `npm update` / `npm audit fix` insufficient due to unused and blocking dependencies.  
- **Examples**:  
  - `react-native-dotenv` (obsolete, replaced by Expo).  
  - Outdated Nativewind requiring peer dependency upgrades.  
- Many unused dependencies and inconsistent configurations.  

---

## 🛠️ The Proper Fix
1. Created a fresh Expo project from template.  
2. Reorganized files and directories.  
3. Reinstalled only **necessary** dependencies.  
4. Migrated to **TypeScript**.  
5. Renamed files to **kebab-case**.  
6. Added **Prettier**.  
7. Added **Dockerized setup** + `.nvmrc` fallback.  

---

## 📚 Major Improvements

### ✅ General Best Practices
- Moved sources from `eml/` → root.  
- Migrated to **TypeScript/TSX** (except configs).  
- Upgraded all dependencies (Expo 54, Node.js 24).  
- Standardized imports (absolute).  
- Removed redundant/legacy files.  
- Updated `.gitignore` to Expo standard.  

### 🎨 Common Platform & Style
- Prettier (`.prettierc`, `.prettierignore`) + full reformat.  
- Added `.editorconfig`.  
- Added `Dockerfile` + `compose.yaml`.  
- Added `.nvmrc`.  
- IDE configurations (JetBrains, VSCode).  
- Arrow functions, TSDoc adoption, exports refactor (WIP).  

---

## 📝 To Do
- Convert more components to **typed props**.  
- Fix failing Jest tests (100+ pass).  
- Full migration to TypeScript + fix `tsc` errors.  
- Migrate tests to `@testing-library/react-native`.  
- Add proper i18n (EN/PT-BR).  
- Migrate `app/index.tsx` → Expo Router.  
- Resolve ESLint warnings.  
- Fix GitHub Workflows.  
- Lock Android client version in Expo config.  

---

## 🚧 Future Issues and Challenges
- **Large PR size**: ~459 files, +67k additions, –80k deletions.  
- Much due to `package-lock.json`, file renaming, formatting.  
- Strategy: **Upgrade first, fix bugs later in smaller batches**.  

---

## 🌿 Branching and Versioning Strategy
- Current: **Gitflow** → dev ahead of main, inconsistent.  
- Proposed: **Trunk-Based Development** (TBD):  
  - Single `main` as source of truth.  
  - Frequent merges (daily).  
  - High-quality PRs required.  
- **Branch Protection**: Lock `main` and enforce PRs.  
- **Versioning**: Use [Semantic Versioning](https://semver.org/) + auto bump on releases.  

---

## ✅ Recommendations
1. Keep using `educado-mobile` repo.  
2. Merge `refactor-and-upgrade` → `dev` ASAP.  
3. Reset `main` = `dev` after upgrade.  
4. Adopt trunk-based development.  
5. Configure branch rulesets.  
6. Fix bugs incrementally with high release velocity.  
7. Release often.  
8. Strengthen CI/CD.  
9. Use **Semantic Versioning**.  
10. Apply similar refactors to other projects.  
11. Gradually fix TypeScript and ESLint issues.  
12. Pause new features until upgrade complete.  
