import { useEffect, useState } from "react";
import axios from "axios";
import "./Dashboard.css";

function ItemsDashboard() {
  const [items, setItems] = useState([]);
  const [showModal, setShowModal] = useState(false);
  const [showEditModal, setShowEditModal] = useState(false);

  const [newItem, setNewItem] = useState({ name: "", quantity: 0 });
  const [editItem, setEditItem] = useState({ id: "", name: "", quantity: 0 });

  // GET items
  const loadItems = () => {
    axios
      .get("http://127.0.0.1:8000/api/items/")
      .then((res) => setItems(res.data))
      .catch((err) => console.error(err));
  };

  useEffect(() => {
    loadItems();
  }, []);

  // CREATE
  const createItem = () => {
    axios
      .post("http://127.0.0.1:8000/api/items/", newItem)
      .then(() => {
        loadItems();
        setShowModal(false);
        setNewItem({ name: "", quantity: 0 });
      })
      .catch((err) => console.error(err));
  };

  // DELETE
  const deleteItem = (id) => {
    if (!window.confirm("¿Eliminar este item?")) return;

    axios
      .delete(`http://127.0.0.1:8000/api/items/${id}/`)
      .then(() => loadItems())
      .catch((err) => console.error(err));
  };

  // UPDATE
  const updateItem = () => {
    axios
      .put(`http://127.0.0.1:8000/api/items/${editItem.id}/`, {
        name: editItem.name,
        quantity: editItem.quantity,
      })
      .then(() => {
        loadItems();
        setShowEditModal(false);
      })
      .catch((err) => console.error(err));
  };

  return (
    <div className="dashboard-container">
      <h1 className="dashboard-title">Items Dashboard</h1>

      <button className="add-btn" onClick={() => setShowModal(true)}>
        + Crear Item
      </button>

      <div className="cards-container">
        {items.map((item) => (
          <div className="card" key={item.id}>
            <h2>{item.name}</h2>
            <p>Cantidad: {item.quantity}</p>

            <div className="card-actions">
              <button
                className="edit-btn"
                onClick={() => {
                  setEditItem(item);
                  setShowEditModal(true);
                }}
              >
                Editar
              </button>

              <button
                className="delete-btn"
                onClick={() => deleteItem(item.id)}
              >
                Eliminar
              </button>
            </div>

            <span className="id-label">ID: {item.id}</span>
          </div>
        ))}
      </div>

      {/* Modal Crear */}
      {showModal && (
        <div className="modal">
          <div className="modal-content">
            <h2>Crear nuevo item</h2>

            <input
              type="text"
              placeholder="Nombre"
              value={newItem.name}
              onChange={(e) =>
                setNewItem({ ...newItem, name: e.target.value })
              }
            />

            <input
              type="number"
              placeholder="Cantidad"
              value={newItem.quantity}
              onChange={(e) =>
                setNewItem({ ...newItem, quantity: Number(e.target.value) })
              }
            />

            <button className="save-btn" onClick={createItem}>
              Guardar
            </button>
            <button className="close-btn" onClick={() => setShowModal(false)}>
              Cerrar
            </button>
          </div>
        </div>
      )}

      {/* Modal Editar */}
      {showEditModal && (
        <div className="modal">
          <div className="modal-content">
            <h2>Editar item</h2>

            <input
              type="text"
              value={editItem.name}
              onChange={(e) =>
                setEditItem({ ...editItem, name: e.target.value })
              }
            />

            <input
              type="number"
              value={editItem.quantity}
              onChange={(e) =>
                setEditItem({ ...editItem, quantity: Number(e.target.value) })
              }
            />

            <button className="save-btn" onClick={updateItem}>
              Actualizar
            </button>
            <button
              className="close-btn"
              onClick={() => setShowEditModal(false)}
            >
              Cerrar
            </button>
          </div>
        </div>
      )}
    </div>
  );
}

export default ItemsDashboard;
