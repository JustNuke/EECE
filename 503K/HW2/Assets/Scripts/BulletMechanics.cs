using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class BulletMechanics : MonoBehaviour
{
    [SerializeField] private GameObject bullets; // Bullet prefab to instantiate
    [SerializeField] private Transform bulletSpawnPoint; // The point where bullets will spawn
    [SerializeField] private float bulletSpeed = 20f; // Speed of the bullet
    [SerializeField] private float shootingCooldown = 0.5f; // Time between shots

    private float lastShotTime = 0f; // Keeps track of the last time a bullet was shot

    void Update()
    {
        // Shooting input (space bar or left mouse button)
        if (Input.GetButtonDown("Fire1") && Time.time >= lastShotTime + shootingCooldown)
        {
            Shoot();
            lastShotTime = Time.time; // Update last shot time
        }
    }

    private void OnCollisionEnter(Collision collision)
    {
        if (collision.gameObject.CompareTag("Enemy"))
        {
            Destroy(gameObject, 3f);
        }
    }

    void Shoot()
    {
        // Instantiate the bullet at the spawn point and set its rotation to the player's rotation
        GameObject bullet = Instantiate(bullets, bulletSpawnPoint.position, bulletSpawnPoint.rotation);

        // Get the Rigidbody component of the bullet and apply force to it
        Rigidbody rb = bullet.GetComponent<Rigidbody>();
        if (rb != null)
        {
            rb.velocity = bulletSpawnPoint.forward * bulletSpeed; // Move bullet forward
        }
    }
}
