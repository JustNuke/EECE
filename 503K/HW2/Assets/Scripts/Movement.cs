using System.Collections;
using System.Collections.Generic;
using System.Diagnostics;
using UnityEngine;
using UnityEngine.EventSystems;
using Debug = UnityEngine.Debug;

public class Movement : MonoBehaviour
{
    [SerializeField] private float speed = 5f;
    [SerializeField] private float rotationSpeed = 720f;

    private Vector3 direction;

    
    void Update()
    {
        HandleMovement();
        HandleRotation();
    }

    void HandleMovement()
    {
        float verticalInput = Input.GetAxis("Vertical"); 
        Vector3 moveDirection = transform.forward * verticalInput; 

        // Move the character
        transform.Translate(moveDirection * speed * Time.deltaTime, Space.World);
    }

    void HandleRotation()
    {
        float horizontalInput = Input.GetAxis("Horizontal"); 
        float rotationAmount = horizontalInput * rotationSpeed * Time.deltaTime; 

        transform.Rotate(Vector3.up, rotationAmount);
    }
}
