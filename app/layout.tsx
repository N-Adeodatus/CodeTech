
import type { Metadata } from 'next'
import './globals.css'
import { Toaster } from '@/components/ui/toaster'
import { cn } from '@/lib/utils'
import { Inter } from 'next/font/google'

const inter = Inter({ subsets: ['latin'], variable: '--font-sans', display: 'swap' })

// Metadata configuration for the application
export const metadata: Metadata = {
  title: 'CodeTech',
  description: 'Interactive learning platform built by the CodeTech Team',
}

// Root layout component that wraps all pages
export default function RootLayout({
  children,
}: Readonly<{ children: React.ReactNode }>) {
  return (
    <html lang="en" suppressHydrationWarning>
      <body className={cn('font-sans antialiased min-h-screen', inter.variable)}>
{children}
<Toaster />
      </body>
    </html>
  )
}
