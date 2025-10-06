## General

- Never use `any`.
- Don't add explicit types to types that can be inferred, e.g., in
  `const [keyboardStatus, setKeyboardStatus] = useState(false);`. TypeScript will know that `keyboardStatus` is a
  boolean without having to annotate `useState<boolean>(false)`. In other words: Don't type more than necessary.

## Component props

Add component prop types as an **interface** to the same file as the component.

**Example**:

```tsx
export interface CourseCardProps {
    title: string;
    length: number;
    content: string;
}

export const CourseCard = ({title, length, content}: CourseCardProps) => {
    // ...
}
```

## Global types

**Rule of thumb**: If a type is used in two or more places, it should be defined as a global type. This rule applies to
all but prop types, which should be defined in the file of the component that uses them.

Place global types in the `types/` directory in a responsibly named file.

**Example**:

```typescript title="types/course.ts"
export type CourseCategory = "recycling" | "safety" | "language";

export interface Course {
    id: string;
    title: string;
    category: CourseCategory;
    durationMin: number;
}
```
