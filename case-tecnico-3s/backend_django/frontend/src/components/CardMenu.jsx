export default function CardMenu({ title, description, onClick }) {
  return (
    <div
      onClick={onClick}
      className="
        bg-secondary border border-border rounded-xl 
        p-6 cursor-pointer 
        hover:border-accent hover:scale-105 
        text-center flex flex-col items-center justify-center
        transition-all duration-300
        w-64 sm:w-72 md:w-80
      "
    >
      <h3 className="text-xl font-semibold mb-2 text-accent">{title}</h3>
      <p className="text-sm text-gray-300">{description}</p>
    </div>
  )
}
