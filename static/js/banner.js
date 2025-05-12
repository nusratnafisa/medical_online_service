// Sample data (replace with real data from your backend)
const items = [
    { type: "doctor", name: "Dr. John Doe", location: "New York" },
    { type: "hospital", name: "City Hospital", location: "Los Angeles" },
    { type: "clinic", name: "Health Clinic", location: "Chicago" },
    { type: "doctor", name: "Dr. Jane Smith", location: "Houston" },
    { type: "hospital", name: "Metro Hospital", location: "Miami" },
    { type: "clinic", name: "Family Clinic", location: "Seattle" }
  ];
  
  function searchItems() {
    const searchInput = document.getElementById("searchInput").value.toLowerCase();
    const resultsDiv = document.getElementById("searchResults");
    resultsDiv.innerHTML = "";
    resultsDiv.classList.remove("show");
  
    if (searchInput === "") {
      return;
    }
  
    const filteredItems = items.filter(item => 
      item.name.toLowerCase().includes(searchInput) || 
      item.location.toLowerCase().includes(searchInput)
    );
  
    if (filteredItems.length > 0) {
      filteredItems.forEach(item => {
        const p = document.createElement("p");
        p.textContent = `${item.name} (${item.type} - ${item.location})`;
        resultsDiv.appendChild(p);
      });
      resultsDiv.classList.add("show");
    } else {
      resultsDiv.innerHTML = "<p>No results found.</p>";
      resultsDiv.classList.add("show");
    }
  }
  
  // Add Enter key support
  document.getElementById("searchInput").addEventListener("keypress", function(event) {
    if (event.key === "Enter") {
      searchItems();
    }
  });
  