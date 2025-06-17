# Accessibility Evaluation Report – Educado

[← Back to Main Page](../../../index.md)

## Introduction

This report assesses the accessibility of the Educado platform (2025.1), covering both mobile and desktop versions. It identifies strengths and areas for improvement that affect users with disabilities, including visual, auditory, motor, and cognitive.

The methodology is based on the *Accessibility Guide for Human-Computer Interaction* (Túlio Celeri), adapted from the *Web Content Accessibility Guidelines* (WCAG), and supported by Nielsen’s usability heuristics. The evaluation includes manual inspection, keyboard navigation testing, contrast verification, and automated tools.

The objective is to contribute to a more inclusive product that respects user diversity and ensures equitable access for all.

## What is Accessibility?

Accessibility refers to designing digital products that are usable by people with diverse disabilities. It ensures content is perceivable, operable, understandable, and robust.

### Benefits

- Social inclusion and participation  
- Legal compliance (e.g., Brazilian Inclusion Law – LBI)  
- Better user experience for everyone  

### Examples

- Alternative text for images  
- Keyboard navigation support  
- Adequate color contrast  
- Captions and transcripts for media  

## Legislation and Guidelines

| Reference                                | Description                                               |
| ----------------------------------------- | --------------------------------------------------------- |
| **Brazilian Inclusion Law (LBI)**         | Guarantees accessibility in digital platforms             |
| **Web Content Accessibility Guidelines**  | International standard for accessibility (W3C/WCAG)       |

## Evaluation Principles

| Principle        | Description                                                                                 |
| ---------------- | ------------------------------------------------------------------------------------------- |
| **Perceivable**  | Content is presented in ways users can perceive (e.g., alt text, captions, contrast)       |
| **Operable**     | Navigation works via various inputs (keyboard, screen readers)                             |
| **Understandable**| Interface is clear, predictable, and easy to understand                                    |
| **Robust**       | Content works with current and future assistive technologies                               |

## Findings

### Positive Findings

| Item                                    | Description                                                                           |
| --------------------------------------- | ------------------------------------------------------------------------------------- |
| **Intuitive Navigation**                | Logical and predictable navigation flow                                               |
| **Clear Content Structure**             | Good visual hierarchy and separation of content                                       |
| **Effective Onboarding**                | Onboarding guides users clearly                                                       |
| **Inclusive Use of Color**              | Avoids using color alone to convey important information                              |
| **Sufficient Contrast (Most Cases)**    | Text and components generally meet contrast requirements                              |
| **Accessible Typography**               | Good font size, weight, and spacing                                                   |
| **Interactive Feedback**                | Visual cues like progress bars and checkmarks support user feedback                   |
| **Progress Indicators**                 | Shows completion status to aid navigation                                             |
| **Adequate Touch Areas (Most)**         | Main interactive areas have appropriate tap size                                      |

### Issues Identified

| Issue                                   | Description                                                                             |
| --------------------------------------- | --------------------------------------------------------------------------------------- |
| **No Screen Reader Support**            | No ARIA labels or semantic tags; inaccessible to blind users                           |
| **Low Contrast in Some Elements**       | Red on blue, yellow on light backgrounds, and white on red fail contrast checks         |
| **Color-Only Feedback**                 | Status like correct/incorrect shown only by color                                      |
| **Overuse of Primary Brand Color**      | Reduces visual focus; lacks clear hierarchy                                             |
| **No Keyboard Focus Indicator**         | No visible indication of focus when navigating by keyboard                              |
| **Inconsistent Learning Flows**         | Some learning activities lack accessible interactions                                   |
| **Missing Alt Text**                    | Icons and images lack alternative text                                                  |
| **Small Touch Targets**                 | Icons like stars and arrows are too small, especially on mobile                         |
| **Semantic Colors Confusing with Brand**| Feedback colors (e.g., error red, success green) clash with brand colors                |

## WCAG Compliance Summary (Complete)

| Guideline                                | Status             | Notes                                                            |
| ----------------------------------------- | ------------------ | ----------------------------------------------------------------- |
| **1.1.1 Non-text Content**                | ❌ Non-Compliant   | Missing alternative text                                         |
| **1.2 Time-based Media**                  | ⚠️ Not Evaluated   | No media (captions, audio descriptions) evaluated                |
| **1.3.1 Info and Relationships**          | ⚠️ Partially       | Visual hierarchy OK; markup and ARIA uncertain                   |
| **1.3.2 Meaningful Sequence**             | ✅ Compliant       | Logical screen flow                                              |
| **1.3.3 Sensory Characteristics**         | ❌ Non-Compliant   | Color-only indicators in feedback                                |
| **1.4.1 Use of Color**                    | ❌ Non-Compliant   | Correct/incorrect shown only by color                            |
| **1.4.3 Contrast (Minimum)**              | ⚠️ Partially       | Some contrast failures                                           |
| **1.4.4 Resize Text / 1.4.10 Reflow**     | ✅ Compliant       | Layout adapts well with zoom                                     |
| **1.4.11 Non-text Contrast**              | ⚠️ Partially       | Some icons and feedback fail contrast                            |
| **2.1.1 Keyboard**                        | ❌ Non-Compliant   | Lacks keyboard support                                           |
| **2.4.3 Focus Order**                     | ⚠️ Partially       | Logical flow inferred; lacks visible focus                       |
| **2.4.4 Link Purpose (In Context)**       | ✅ Compliant       | Buttons/links labeled correctly                                  |
| **2.4.7 Focus Visible**                   | ❌ Non-Compliant   | No visible keyboard focus                                        |
| **2.5.1 Pointer Gestures**                | ✅ Compliant       | Touch targets large; gestures simple                             |
| **2.5.5 Target Size**                     | ⚠️ Partially       | Main buttons OK; minor icons too small                           |
| **3.2.3 Consistent Navigation**           | ✅ Compliant       | Navigation consistent across screens                             |
| **3.3.1 Error Identification**            | ⚠️ Partially       | Errors shown with color only; lacks text/icons                   |
| **4.1.2 Name, Role, Value**               | ❌ Non-Compliant   | No ARIA roles; inaccessible to assistive tech                    |
| **4.1.3 Status Messages**                 | ❌ Non-Compliant   | No coded status feedback                                         |
| **Multiple Other WCAG Criteria**          | ⚠️ Not Evaluated   | Includes parsing, language, input behavior, error prevention     |

## Evaluation Limitations

This evaluation prioritized the most impactful criteria for visual, structural, and interactive accessibility. However, the following WCAG criteria were **not fully evaluated**:

- **Time-based media:** No analysis of captions, transcripts, or audio descriptions (Guideline 1.2).  
- **Language declaration:** No check for page or section language (3.1.1, 3.1.2).  
- **Error prevention in forms:** Not verified if forms prevent critical errors (3.3.4).  
- **Parsing and code robustness:** No verification of semantic code structure (4.1.1).  
- **Navigation aids:** Skip links and multiple navigation methods were not evaluated (2.4.1, 2.4.5).  

A full WCAG compliance audit should include these elements in future iterations.

## Recommendations

| Area                              | Action                                                                             | Priority |
| --------------------------------- | ---------------------------------------------------------------------------------- | -------- |
| **Screen Reader Support**         | Implement ARIA roles and semantic HTML, add alt text                               | High     |
| **Keyboard Navigation**           | Add visible focus indicators and ensure logical tab order                          | High     |
| **Contrast Fixes**                | Correct contrast failures in feedback and text                                     | High     |
| **Feedback Beyond Color**         | Add text, icons, or patterns to supplement color indicators                        | High     |
| **Alt Text for Media**            | Apply descriptive alternative text to images and icons                             | Medium   |
| **Touch Target Size**             | Adjust small icons and controls to meet minimum size                               | Medium   |
| **Brand Color Optimization**      | Reduce overuse and improve hierarchy with varied color usage                       | Medium   |
| **Learning Flow Consistency**     | Ensure activities like quizzes are accessible and follow WCAG principles            | Medium   |
| **Parsing and Code Robustness**   | Validate HTML semantics and fix markup for assistive technology support             | Medium   |
| **Language Metadata**             | Add `lang` attribute to the page and content parts with different languages         | Medium   |
| **Error Prevention in Forms**     | Implement confirmation steps in sensitive actions (financial, legal, data)          | Medium   |

## Next Steps

1. Apply semantic HTML, ARIA roles, and alternative text.  
2. Fix contrast issues and avoid color-only feedback.  
3. Improve keyboard accessibility with visible focus and logical order.  
4. Expand touch targets where needed.  
5. Optimize color usage for hierarchy.  
6. Validate code for parsing errors and semantic correctness.  
7. Declare language metadata for pages and content.  
8. Improve error prevention in forms.  
9. Conduct usability testing with users with disabilities.  

## Conclusion

The Educado platform demonstrates solid design foundations but presents critical accessibility gaps that prevent full inclusion for users with disabilities. Addressing the identified issues will ensure compliance with accessibility standards and improve the user experience for everyone. A future complete audit should expand the evaluation to include additional WCAG success criteria not covered in this report.

## Revision History

| Date       | Version | Changes                      | Authors                                      |
| ---------- | ------- | ---------------------------- | -------------------------------------------- |
| 17/06/2025 | 1.0     | Initial Accessibility Report | [Luísa Leão](https://github.com/lluisalleao) |

[← Back to Main Page](../../../index.md)
