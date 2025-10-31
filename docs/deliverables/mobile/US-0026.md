# View Course Catalog

## Overview  
This PBI introduces a visual overhaul of the exlore page and its contents. 

---

## User Story  
As a Student, I want to see a catalog of available courses, so that I can explore what I can learn.

---

## What Was Implemented  
 - Items aligned in explore cards
 - Reversed the order in which cards are shown
 - Changed category labels as well as button colors to match Figma
 - Updated searchbar and header
 - Removed unused files [FilteringOptions.jsx, AccessCourseButton.tsx, ActiveExploreCard.tsx, CourseView.tsx, SubscriptionButton.tsx, updateDate.tsx]
 - Visual indicator for course enrollment
 - Minor improvements to code and component structure
 - Reusable CourseButton replaces several button components
 - Transitioned to TypeScript
---

## Impact  
This delivery will impact the user experience, as the new design is more comprehensible and clear. Furthermore, some of the structural changes has increased the codebases comprehensibility and complexity, making it easier to maintain.  

---

## Related Files / Modules  
- screens/Explore/ExploreScreen.tsx
- components/explore
- components/general/BaseScreen.tsx
- components/general/IconHeader.tsx
- i8n/locales/en-US.json
- i8n/locales/pt-BR.json
- services/utils.ts
- theme/typography.tokens.json
- theme/typography.ts
- types/icon.ts
---

**Team:** Mobile - Gruppe 2 
**Date:** 10/28/2025