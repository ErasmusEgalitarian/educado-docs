## Use `PascalCase` for component names, files, and directories

**Rationale**: This is the Expo standard.

**Example**: Component `MyClassyList` is in `components/Courses/MyClassyList.tsx`.

## Use `kebab-case` for regular TypeScript files and directories

**Rationale**: This is the TypeScript standard.

**Example**: `services/certificate-service.ts`.

## Use the Expo notation in the `app/` directory

**Rationale**: This is the Expo standard. Read more [here](https://docs.expo.dev/router/basics/notation/).

**Example**: `app/_layout.tsx`.

## Name tests `FILENAME-test.{ts,tsx}`

**Rationale**: This is the Expo standard.

**Example**: `LeaveButton-test.tsx`

## Match component file names to component names

**Rationale**: Components are easier to find.

**Example**: Component `CompleteCourseScreen` is in `CompleteCourseScreen.tsx`

## Use arrow functions

**Rationale**: This is the modern JavaScript/TypeScript approach to function declaration.

!!! note

    This rule is enforced by ESLint.

## Use [TSDoc](https://tsdoc.org/) for function documentation

**Rationale**: Proper function documentation is very helpful and TSDoc can be read by IDEs. You will be able to read the
function documentation at the call site in the IDE. See the example below.

![TSDoc example](../../assets/handbook/mobile/tsdoc-tooltip.png){: style="height:300px"}

## Use `.tsx` for components, `.ts` for other files

**Rationale**: Always prefer TypeScript extensions and match them to the purpose of the file. Unless a file contains
JSX code (e.g., code like `<Component />`), it doesn't need to use the `.tsx` extension.

## Never do `import React from "react";`

**Rationale**: The new JSX transform (React 17+) doesn't require importing React in scope. React doesn't need to be in
scope. Importing React is usually unused noise; omit it to keep files clean.

!!! note

    This rule is enforced by ESLint.

## Use absolute imports

**Rationale**: Absolute imports are more readable and easier to refactor.

**Example**:

❌ `import { getUserInfo } from "../../../services/storage-service";`

✅ `import { getUserInfo } from "@/services/storage-service";`

!!! note

    This rule is enforced by ESLint.

## Don't use `any`

**Rationale**: Using `any` is the same as turning off type checking and using JavaScript. If the "no-type" is allowed,
why even bother with the TypeScript type system?

See the official
[TypeScript docs](https://www.typescriptlang.org/docs/handbook/declaration-files/do-s-and-don-ts.html#any) for more
information.

!!! note

    This rule is enforced by ESLint.

## Don't use `useCallback` or `useMemo`

**Rationale**: These hooks are not necessary when React 19+ is used. The new React Compiler will automatically memoize
values, making `useCallback` and `useMemo` redundant.

See the official [React Compiler docs](https://react.dev/learn/react-compiler/introduction) for more information.

!!! note

    This rule is enforced by ESLint.

## Use named exports, except in the `app/` directory

**Rationale**: Named imports require the imported symbol to have the same name as the exported symbol. This eases
finding components and files.

**Example**:

```tsx
export const MyComponent = () => {
    // ...
};
```

**Exception**:

Expo Router needs default exports in the `app/` directory. For that reason, default exports are allowed in the `app/`
directory and should be placed at the bottom of the file.

```tsx title="app/(tabs)/course/index.tsx"
const Course = () => {
    // ...
};

export default Course;
```

!!! note

    This rule is not enforced by ESLint yet, as it would require a lot of refactoring. Files where components are
    imported would have to be refactored e.g., from `import ExerciseScreen from "@/screens/Excercises/ExerciseScreen";` 
    to `import { ExerciseScreen } from "@/screens/Excercises/ExerciseScreen";`. This rule will be enforced in the
    future. Default exports should be refactored to named exports incrementally.

## Use inline exports, except in the `app/` directory

**Rationale**: Inline exports prevent merge conflicts at the bottom of the file. Also, it's harder to forget to export
when the export is on the same line as the declaration.

**Example**:

```tsx
export const SomeStuff = ({name, age, height}: SomeStuffProps) => {
    // ...
}
```

**Exception**:

Expo Router needs default exports in the `app/` directory. For that reason, default exports are allowed in the `app/`
directory and should be placed at the bottom of the file.

```tsx title="app/(tabs)/course/index.tsx"
const Course = () => {
    // ...
};

export default Course;
```

## Use descriptive, full names

**Rationale**: `NavigationBar` is more readable than `NavBar`. `WelcomeScreenAcceptButton` is more descriptive than
`GreenButton`.

## Only one component per file

**Rationale**: Smaller files mean fewer merge conflicts, easier editing, easier deletion.

!!! note

    Tiny internal helpers are okay if they're tightly coupled and not reused.

## Use the Android emulator and correct Android API version

**Rationale**: The end users use Android devices, and we should develop on and target this platform. Using the Android
emulator gives us the opportunity to emulate real Android hardware and scenarios. Also, all developers should develop on
the same platform. The platform should match the Expo and system requirements. Currently, we use Expo 54, Node.js 20 and
Android SDK 35, the upgrade to Node.js 24 is still in progress.

## Use nvm or Docker for local development

**Rationale**: See previous point.

## Never use PropTypes, use the TypeScript type system

**Rationale**: The `prop-types` package is an ancient, deprecated way of typing props. Always use TypeScript interfaces.
See the [Typing section](./typing.md) for more information.

!!! note

    This rule is enforced by ESLint.

## Use localization

**Rationale**: Never hardcode values, especially not locale-specific string. Make them dynamic, so developers can switch
language. This doesn't mean that the end users will be able to switch languages. We will lock the deployed app to
Brazilian Portuguese. Read more in the [Expo docs](https://docs.expo.dev/guides/localization/).

**Example**:

Always add a translation string to the two translation files in `i18n/locales/`.

```json title="i18n/locales/en-US.json"
{
    "welcome": {
        "greeting": "We love Educado"
    }
}
```

```json title="i18n/locales/pt-BR.json"
{
    "welcome": {
        "greeting": "Nós amamos o Educado"
    }
}
```

You can then access the dynamic translation string in a component like this:

```tsx title="components/.../MyTextComponent.tsx"
import {t} from "@/i18n";

const MyTextComponent = () => {
    return <Text>{t("welcome.greeting")}</Text>;
}
```

## Only use the Expo CLI to install dependencies

**Rationale**: Expo is very picky about dependencies and has its own package management interface `npx expo install`.
Always prefer it to direct `npm` calls whenever possible. Read more in the
[Expo docs](https://docs.expo.dev/more/expo-cli/#install).

## Never run `npm update`

**Rationale**: `npm update` is not fully compatible with Expo, as Expo needs precise versions of packages. Packages
should only be updated using `npx expo install --check`, or manually (individual packages), but even that is cumbersome.
If you believe that an update is necessary, consult the mobile tech lead.

## Never import the Tailwind config into a component

**Rationale**: The bundle size explodes when the Tailwind config is imported into a component. Import color tokens
directly or create custom Tailwind classes. If you edit and import colors, change the color values in
`tailwind.config.js` and in `theme/colors.ts`. The values in the latter file should be kept in sync with the values in
the former file. Nativewind will read the values from `tailwind.config.js`, while components will reference the values
from `theme/colors.ts`.

**Example**:

❌

```tsx
import tailwindConfig from "../../tailwind.config.js";

const tailwindColors = tailwindConfig.theme.colors;
```

❌

```tsx
const tailwindConfig = require("../../../tailwind.config.js");

const projectColors = tailwindConfig.theme.colors;
```

✅

```tsx
import {colors} from "@/theme/colors";

export const BackgroundLinearGradient = ({children}) => {
    return (
        <LinearGradient
            colors={[colors.bgPrimary, colors.projectWhite]}
        />
    );
}
```

!!! note

    As we progress with the upgrade, the color values from `theme/colors.ts` will be imported into `tailwind.config.ts`,
    but that is not possible yet. That's why the two `colors` objects need to be kept in sync for now.

!!! note

    This rule is enforced by ESLint. Refactor `tailwind.config.js` imports to a tokens import when you see it.

## Read the official documentation

**Rationale**: The official
[Expo](https://docs.expo.dev/), [Nativewind](https://www.nativewind.dev/), [Jest](https://jestjs.io/),
[TypeScript](https://www.typescriptlang.org/), and [Axios](https://axios-http.com/) docs will get you far, very far.

## Use standard commit messages

**Rationale**: GitHub reads keywords in commit messages and closes issues when a PR is merged that contains commit
messages that use those keywords. Furthermore, adding the issue ID to the commit message links the commit to the issue.
Finally, your commit message should finish the sentence: `If applied, this commit will [your commit message goes here]`.

**Example**: `Fix #34. Add the new welcome banner`. This commit message will link this commit to issue #34 and close
this issue when the commit is merged.

## Communicate, communicate, communicate

**Rationale**: We need to work efficiently and with a high cadence. Surprises are not as good as knowledge. Be kind to
each other.

**Example**: Follow what's going on GitHub, check PRs, ask questions, ask questions on Discord and follow `# mobile`,
read the docs and update them if necessary.

## Only commit what you actually worked on

**Rationale**: Random changes shouldn't be included in VCS. Don't blindly use `git add .`. Use `git status` to check
which files Git detects as modified. Only `git add` what you actually want to add.
