import { DataTypes, Model, Optional } from 'sequelize';
import sequelize from '../config/database';

// Definir los atributos del modelo
interface EmpresaAttributes {
  id: number;
  nombre: string;
  descripcion?: string;
  email?: string;
  telefono?: string;
  activo: boolean;
  created_at?: Date;
  updated_at?: Date;
}

// Atributos opcionales para creación
interface EmpresaCreationAttributes extends Optional<EmpresaAttributes, 'id'> {}

// Extender Model
class Empresa extends Model<EmpresaAttributes, EmpresaCreationAttributes> 
  implements EmpresaAttributes {
  public id!: number;
  public nombre!: string;
  public descripcion?: string;
  public email?: string;
  public telefono?: string;
  public activo!: boolean;

  // timestamps
  public readonly created_at!: Date;
  public readonly updated_at!: Date;
}

// Inicializar el modelo
Empresa.init(
  {
    id: {
      type: DataTypes.INTEGER,
      autoIncrement: true,
      primaryKey: true,
    },
    nombre: {
      type: DataTypes.STRING(255),
      allowNull: false,
    },
    descripcion: {
      type: DataTypes.TEXT,
      allowNull: true,
    },
    email: {
      type: DataTypes.STRING(255),
      allowNull: true,
      validate: {
        isEmail: true,
      },
    },
    telefono: {
      type: DataTypes.STRING(50),
      allowNull: true,
    },
    activo: {
      type: DataTypes.BOOLEAN,
      defaultValue: true,
    },
  },
  {
    sequelize,
    tableName: 'empresas', // Nombre de la tabla en la BD
    timestamps: true,
    underscored: true,
  }
);

export default Empresa;
