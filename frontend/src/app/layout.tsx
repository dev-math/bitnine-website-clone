import "@/styles/globals.css";
import "@radix-ui/themes/styles.css";
import { Theme } from "@radix-ui/themes";
import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "AgensSQL ⋆ Bitnine Global Inc.",
  description:
    "AgensGraph is a fast, reliable graph database platform with high relational compatibility. As the only multi-model graph database integrated with PostgreSQL, AgensGraph enables flexibility with proven relational database features, scale and performance for enterprises.",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body>
        <Theme appearance="light" panelBackground="solid" radius="large">
          {children}
        </Theme>
      </body>
    </html>
  );
}
