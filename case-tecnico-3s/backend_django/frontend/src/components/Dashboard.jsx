export default function Dashboard({ children }) {
  return (
    <div className="min-h-screen bg-gray-900 text-white flex flex-col items-center justify-center">
      <div className="grid grid-cols-1 sm:grid-cols-2 gap-6 place-items-center">
        {children}
      </div>
    </div>
  )
}
